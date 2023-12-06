import random

chance = 5
running = True
print("Enter the number between 1 - 10")
while running:
    inp = int(input('Enter the number: '))
    x = random.randrange(1,10)
    if inp == x:
        print('computer is:',x,'you:',inp)
        print('You won the game!')
        running=False
    chance = chance-1
    print('Try again!')
    print('Chances left:',chance)
    if chance == 0:
        print('You lose!')
        running =False

print('Game finished')