m1 = int(input("enter the first subject mark: "))
m2 = int(input("enter the second subject mark: "))
m3 = int(input("enter the three subject mark: "))
m4 = int(input("enter the four subject mark: "))
m5 = int(input("enter the five subject mark: "))

count = 0
totalmark = 0
for marks in [m1,m2,m3,m4,m5]:
    count = count +1
    totalmark = totalmark+marks
    print(count,totalmark)
print("Total subject:",count,"Total marks:",totalmark,'Average:',totalmark/count)