
def RotateArray(arr,index):
    s=len(arr)
    print("before rotating : ")
    print(arr)
    index=index%s
    for i in range(0,index):
        temp=arr[0]

        for j in range(0,s-1):
            arr[j]=arr[j+1]

        arr[j+1]=temp
        

    print("Äfter Rotating :")
    print(arr)       
    return arr

def countRotation(k,rArr):
     for i in range(0,len(rArr)):
         if(k==rArr[i]):
             t=i
     t=len(rArr)-t
     print("Array is rotated by "+str(t)+" times or multiple of "+str(t))


arr1=[[1,2,3,4,5,6,7,8,9],[23,45,67,89,96],[1,4,7,9,12,34]]
for i in range(0,len(arr1)):
    originalArray=[x for x in arr1[i]]
    n=originalArray[2]
    k= int(input("Give key for rotating : "))
    rotatedArray=RotateArray(arr1[i],k)
    countRotation(originalArray[0],rotatedArray)
    print("*****************************************************")
    print("*****************************************************")