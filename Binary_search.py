def binarySearch(arr,n):
    first=0
    last=len(arr)
    while(True):
        mid=int((first+last)/2)
        if(arr[mid]==n):
            print(str(mid)+" is the index at which "+str(n)+" is found")
            return arr[mid]
        elif(arr[mid]<n):
            first=mid
            last=last
    
        elif(arr[mid]>n):
            first=first
            last=mid
        else:
            print("Element is not present in this array")     
            return  "NOT PRESENT"

arr1=[[1,2,3,4,5,6,7,8,9],[23,45,67,89,96],[1,4,7,9,12,34]]
for i in range(0,len(arr1)):
    originalArray=[x for x in arr1[i]]
    print(originalArray)
    n=int(input("Give element to Search : "))
    t=binarySearch(arr1[i],n)
    if(t=="NOT PRESENT" or t!=n):
        if(t=="NOT PRESENT"):
            print("ELEMENT IS NOT Present in the ARRAY")
        else:
            print("Binary Search is not working properly")