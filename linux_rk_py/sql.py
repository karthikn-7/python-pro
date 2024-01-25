rk = 'karthik'
vk = 'vinoth'
lst = [1,3,4,6,6,6,6,rk,vk,rk,rk,vk]


rkcount = 0
vkcount = 0
for cont in lst:
    if cont == rk:
        rkcount+=1
    elif cont == vk:
        vkcount+=1
    else:
        pass

if rkcount > vkcount:
    
    print(rk,'wins')
elif rkcount < vkcount:
    print(vk,'wins')
else:
    print('draw')
