# enqueue of the queue 
def enqueue():
    print()
    enq = input('Enter The Element To Be Added: ')
    queue.append(enq)
    print(f'ELement {enq} Added!')
    print()
# dequeue of the queue
def dequeue():
    print()
    if len(queue) == 0:
        print('Queue is Empty!')
    else:
        
        print(f'Element {queue[0]} is Deleted!')
        del queue[0]
    print()
# display of the queue
def display():
    print()
    if len(queue) == 0:
        print('Queue is Empty!')
    else:
        print('The Elements In The Queue Are:')
        for ele in queue:
            print(ele,end =" ")
    print()
    print()


queue = list()

while (1):
    print('(1) FOR ENQUEUE\n(2) FOR DEQUEUE\n(3) FOR DISPLAY\n(4) FOR EXIT')
    inp = int(input('Enter The Option: '))

    # enqueue
    if inp == 1:
        enqueue()
    
    # dequeue
    if inp == 2:
        dequeue()
    
    # diplay the elements
    if inp == 3:
        display()
    
    # stopping of the program
    if inp == 4:
        print('Program Stopped!')
        break
    
    # for invalid option
