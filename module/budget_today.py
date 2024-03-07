#budget today
def budget_today(total_amount:int) -> int:
    '''
    This module helps u find daily expenses. out of how much
    money did you take with you!
    '''
    total = 0
    ea = 0
    ta = total_amount
    print('Double Enter to See the result!')
    print()
    while True:
        try:
            amount = int(input("Enter amount: "))
            total += amount
            ra = ta - total
            if total > ta:
                ea = total - ta
            else:
                pass                

        except:
            print()
            print(f'Total amount Today You have spent: {total}.of {ta}')
            try:
                if ra > 0:
                    print(f"Remaining: {ra}")
                else:
                    print(f'Extra Expenses today: {ea}')
                break
            except:
                break
                
