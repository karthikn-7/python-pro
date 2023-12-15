
array = [1, 3, 2, 1, 4, 1] 

maxfreq = 0
for i in range(len(array)):
    if array.count(array[i])  >  array.count(maxfreq):
        maxfreq = array[i]
    
print(maxfreq)

