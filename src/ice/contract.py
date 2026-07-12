class Contract:
    def __init__(self, src, dst, expression):
        self.src = src
        self.dst = dst
        self.expression = expression
    
    def evaluate(self):
        return self.expression(self.src, self.dst)
