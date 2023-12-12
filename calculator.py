class Calculator:
    def __init__(self,a=10,b=10):
        self.a = a
        self.b = b
        
    def addition(self):
        add = self.a +self.b
        print('add:',add)

    def subtraction(self):
        sub = self.a - self.b
        print('sub:',sub)
        
    def multiplication(self):
        mult = self.a * self.b
        print('mult:',mult)
        
    def divison(self):
        div = self.a / self.b
        print('div:',div)
        
class CalUpdate(Calculator):
    def __init__(self):
        super().__init__()
    
    def sqrs(self):
        sqr = self.a ** self.b
        print('sqr:',sqr)
        pass

calculation = CalUpdate()
calculation.subtraction()