class Calculator:
    def __init__(self):
        pass
    def add(self,x1,x2):
        return x1+x2
    def multiply(self,x1,x2):
        return x1*x2
    def divide(self,x1,x2):
        if x2 != 0:
            return x1/x2
        else: print("Error, на ноль делить нельзя!")
    def minus(self,x1,x2):
        return x1-x2