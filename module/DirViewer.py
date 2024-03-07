def DirViewer(object):
    count = 1
    for i in dir(object):
        
        if '__' not in i:
            print(count, i,sep=':')
            count = count+1

DirViewer()
