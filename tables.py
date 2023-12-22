inp = int(input('Enter the Table: '))
timesinp = int(input('Enter the times: '))
times= inp*timesinp
lst = []
for i in range(inp,times+1,inp):
    lst.append(i)

print(lst)