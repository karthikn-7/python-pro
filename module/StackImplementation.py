# last in first out

class Stack:
    def __init__(self):
        self.__list = []
    
    def push(self,element):
        PushedElement = self.__list.append(element)
        print(f'Pushed ELement is: {element}')
        print('+++++++++++++++++++')
        
    
    def peek(self):
        if len(self.__list) == 0:
            print('Stack is empty!')
            print('---------------')
        else:
            print(f'Top Element is {self.__list[-1]}')
            
    
    def pop(self):
        if len(self.__list) == 0:
            print('Stack is empty!')
            print('---------------')
        else:
            poppedelemt = self.__list.pop()
            print(f'Popped Element is: {poppedelemt}')
            print('-------------------')
        
    def isEmpty(self):
        if len(self.__list) == 0:
            print('Stack Is Empty')
            print('--------------')
    
            
stack1 = Stack()

stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.peek()

