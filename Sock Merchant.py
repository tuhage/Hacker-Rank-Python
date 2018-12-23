def sockMerchant(n, ar):
    ar.sort()
    count=0
    print(ar)
    i=0
    while(i<n-1):
        if ar[i]==ar[i+1]:
            count+=1
            i+=2
        else :
            i+=1
    return count

print(sockMerchant(20, [4 ,5, 5 ,5, 6 ,6 ,4 ,1 ,4, 4, 3 ,6, 6 ,3, 6 ,1 ,4, 5 ,5 ,5]))