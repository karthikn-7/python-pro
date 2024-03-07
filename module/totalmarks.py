number = list()
while True:
    inp = input('Enter the number: ')
    if inp == 'done':
        break
    inp = float(inp)
    number.append(inp)
print(number)
print(sum(number)/len(number))
    