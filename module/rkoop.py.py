class rockkarthik():
    def __init__(self,name,age,a,b):
        self.name = name
        self.age = age
        self.a = a
        self.b = b
    
    def peron(self):
        print("hi",self.name)
        print("You are:",self.age,"years old")
        
    def next_birthday(self):
        newage = self.age + 1
        print("Your next age is:",newage)
        print("enjoy your",newage,"st birthday!")
        
    def additionOf_twonums(self):
        addition = self.a + self.b
        print("the addition of two numbers is:",addition)
        
    def is_male(self):
        if self.name == 'karthik':
            print("he is male")
        elif self.name == 'vinoth':
            print("we are all know that he is female!")
            
    def subractionOf_twonums(self):
        subtraction = self.a - self.b
        print("subtracted number is:",subtraction)
        
    def is_teenage(self):
        try:
            if self.age >= 18:
                print("you are now adult ! be responsible")
            else:
                print("you are teenage! Enjoy it")
        except:
            print("its a invalid input!, Only numbers allowed in age!")

