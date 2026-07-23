"""Convert schema dumps into usable data structures."""

import re

from ice.engine.model import (
    And, Or, Not,
    Capability, DynamicCapability,
    RemoteSystem, System, LocalSystem,
    Requirement
    )

TOKEN_RE = re.compile(r'\(|\)|and|or|not|[A-Za-z_][A-Za-z0-9_]*')
KEYWORDS = {"and", "or", "not", "(", ")"}


def tokenise(expr):
    return TOKEN_RE.findall(expr)

class Parser:
    """Build contract from tokenised expression."""
    def __init__(self, tokens, capabilities_by_name):
        self.tokens = tokens
        self.pos = 0
        self.capabilities_by_name = capabilities_by_name

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def advance(self):
        tok = self.peek()
        self.pos += 1
        return tok

    # Build OR node, low precedence
    def parse_expr(self):
        node = self.parse_term()
        while self.peek() == "or":
            self.advance()
            node = Or(node, self.parse_term())
        return node

    # Build AND node, medium precendence
    def parse_term(self):
        node = self.parse_factor()
        while self.peek() == "and":
            self.advance()
            node = And(node, self.parse_factor())
        return node

    # Build not node, high precedence
    def parse_factor(self):
        tok = self.peek()
        if tok == "not":
            self.advance()
            return Not(self.parse_factor())
        if tok == "(":
            self.advance()
            node = self.parse_expr()
            self.advance()
            return node
        self.advance()
        return self.capabilities_by_name[tok]

def build(configuration):

    systems_by_name = {}
    capabilities_by_name = {}

    local_system = LocalSystem("ice")

    for entry in configuration["systems"]:
        # Build system
        name = entry["name"]
        
        # Set connection attributes
        if target := entry.get("target", None):
            username = entry["username"]
            password = entry["password"]
            system = RemoteSystem(name, target, username, password)
        else:
            system = System(name)

        systems_by_name[name] = system

    for entry in configuration["capabilities"]:
        # Get system
        name = entry["name"]
        system = systems_by_name[entry["system"]]

        # Set probe attributes
        if cmd := entry.get("cmd", None):
            # Resolve origin
            match origin_name := entry.get("origin", None):
                case None:
                    origin = system
                case "ice":
                    origin = local_system
                case _:
                    origin = systems_by_name[origin_name]
            capability = DynamicCapability(name, system, origin, cmd)
        else:
            # Set immutable state
            origin = system
            capability = Capability(name, system, origin)
            capability.state = entry["state"]

        # Add capability to capabilities_by_name
        capabilities_by_name[name] = capability
        origin.probes.append(capability)

    for entry in configuration["requirements"]:
        name = entry["name"]
        system = systems_by_name[entry["system"]]

        # Create contract
        tokens = tokenise(entry["contract"])
        contract = Parser(tokens, capabilities_by_name).parse_expr()

        # Get capability list
        capability_names = [t for t in tokens if t not in KEYWORDS]
        capabilities = [capabilities_by_name[n] for n in capability_names]

        # Add requirement to system
        requirement = Requirement(name, system, capabilities, contract)
        system.requirements.append(requirement)

        # Create requirement-capability mapping
        for capability in capabilities:
            requirement.capabilities.append(capability)
            capability.requirements.append(requirement)

    return list(systems_by_name.values()) + [local_system]
