class Contract:
    def __init__(self, src, dst, lcl, expression):
        self.src = src
        self.dst = dst
        self.lcl = lcl
        self.expression = expression
    
    def evaluate(self):
        return self.expression(self.src, self.dst, self.lcl)
