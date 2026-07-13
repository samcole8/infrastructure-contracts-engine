class And:
    def __init__(self, *operands):
        self.operands = operands

    def evaluate(self):
        results = [o.evaluate() for o in self.operands]
        if False in results:
            return False          # any confirmed False wins outright
        if None in results:
            return None           # no False, but something unresolved
        return True                # all confirmed True


class Or:
    def __init__(self, *operands):
        self.operands = operands

    def evaluate(self):
        results = [o.evaluate() for o in self.operands]
        if True in results:
            return True           # any confirmed True wins outright
        if None in results:
            return None           # no True, but something unresolved
        return False               # all confirmed False


class Not:
    def __init__(self, operand):
        self.operand = operand

    def evaluate(self):
        result = self.operand.evaluate()
        return None if result is None else not result


class Contract:
    def __init__(self, name, src, dst, expression):
        self.name = name
        self.src = src
        self.dst = dst
        self.expression = expression

    def evaluate(self):
        return self.expression.evaluate()
