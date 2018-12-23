def bonAppetit(bill, k, b):
    sum=0
    for i in range(len(bill)):
        if(i==k):
            continue
        sum+=bill[i]
    pay=sum/2
    charge=b-pay
    if(charge==0):
        return print("Bon Appetit")
    else :
        print( int(charge))

bonAppetit((3,10,2,9),1,12)