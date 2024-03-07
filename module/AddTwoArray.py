def addingarr(arr1,arr2):
    lst = []
    if len(arr1) != len(arr2):
        return -1

    for i in range(len(arr1)):
        lst.append(arr1[i]+arr2[i])
    return lst
