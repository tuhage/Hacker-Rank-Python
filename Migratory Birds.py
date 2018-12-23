def migratoryBirds(arr):
    count={1:0,2:0,3:0,4:0,5:0}

    for i in arr:
        if i==1 :
            count[1]+=1
        if i==2 :
            count[2]+=1
        if i==3 :
            count[3]+=1
        if i==4 :
            count[4]+=1
        if i==5 :
            count[5]+=1

    max=count[1]

    for i in range(2,6):
        n=int(count[i])
        if max < n :
            max = n
            maxi=i

    return maxi


a=(1,2,3,4,3,5,5,3,5,5,5,5,5,1,2)

print(migratoryBirds(a))