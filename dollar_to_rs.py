
try:
    while True:
        dollar = input('Enter the usa dollar: ')
        dollar = int(dollar)
        ind_rs = 83.22
        dol_to_rs = ind_rs*dollar
        print('indian rs:',dol_to_rs)
except:
    print("only valid within 100rs input!")
    

