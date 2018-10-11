    arrLength=len(arr)
    countminus=0
    countplus=0
    countzero=0
    for i in arr:
        if i<0:
            countminus+=1
        elif i>0:
            countplus+=1
        else:
            countzero+=1

    print("{0:.6f}".format(countplus/arrLength))
    print("{0:.6f}".format(countminus/arrLength))
    print("{0:.6f}".format(countzero/arrLength))


