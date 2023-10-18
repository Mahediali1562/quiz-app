l1 = [3456,23,128,235,982]
l2 = [2,3,5,4]
l3={0}
for i in range(0,5):
    k=l1[i]
    while(l1[i]):
        x=l1[i]%10
        if(x==2 & x==3 & x==5 & x==4):
        c=c+1
        l1[i]=l1[i]/10


print(l3)