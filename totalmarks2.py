total = 0
count = 0
while True:
    inp = input('enter the number: ')
    if inp == 'done':  break
    total = total+float(inp)
    count = count+1
avg = total/count
print('subjects:',count,'total marks:',total,'average:',avg)
print('done')