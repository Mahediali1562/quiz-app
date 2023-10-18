arr1= [3,4,12,13,56,36,6,67,34]
arr2=[13,56,36,67]
arr3={0}
arr3.remove(0)
k=0
for i in range(0,9):
    for j in range(0,4):
        if(arr1[i]==arr2[j]):
            i=i+1


    arr3.add(arr1[i])
    k = k + 1



print(arr3)
