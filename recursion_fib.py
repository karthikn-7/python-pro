def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input('enter the number: '))
print(f'fibonacci series upto {n} is:')
lst = []
for i in range(n):
    lst.append(fib(i))
    
print(lst)