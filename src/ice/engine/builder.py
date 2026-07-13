"""Convert schema dumps into usable data structures."""

import re

from ice.scm import And, Or, Not
from ice.scm import System, Capability, Requirement
from ice.engine.probe import Probe


TOKEN_RE = re.compile(r'\(|\)|and|or|not|[A-Za-z_][A-Za-z0-9_]*')

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

def build_contract(contract_expression, capabilities_by_name):
    tokens = tokenise(contract_expression)
    return Parser(tokens, capabilities_by_name).parse_expr()

def build(configuration):

    systems_by_name = {}
    capabilities_by_name = {}
    probes = []

    for entry in configuration["systems"]:
      name = entry["name"]
      systems_by_name[name] = (System(name))

    for entry in configuration["capabilities"]:

        # Create capability
        name = entry["name"]
        src = systems_by_name[entry["src"]]
        dst = systems_by_name[entry["dst"]]
        capability = Capability(name, src, dst)
        
        # Check for probe
        check = entry.get("check", None)
        if check:
            # Create probe
            origin = entry.get("origin", "src")
            probes.append(Probe(capability, check, origin))
        else:
            #  Set stateits
            state = entry.get("state", None)
            capability.state = state

        # Add capability to system
        src.capabilities.append(capability)

        # Add capability to capabilities_by_name
        capabilities_by_name[name] = capability

    for entry in configuration["requirements"]:

        # Create requirement
        name = entry["name"]
        src = systems_by_name[entry["src"]]
        contract = build_contract(entry["contract"], capabilities_by_name)

        # Add requirement to system
        src.requirements.append(Requirement(name, src, contract))

    return tuple(systems_by_name.values()), probes
