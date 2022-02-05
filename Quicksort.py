def Quicksort(l,h,arr):
    if(l<h):
        k=partition(l,h,arr)
        print(k)
        Quicksort(l,k-1,arr)
        Quicksort(k+1,h,arr)
    

def partition(l,h,arr):
    pivot=arr[l]
    i=l+1 
    j=h
    while(i<j):
        while(i<len(arr)):
            if(arr[i]>=pivot):
                break;
            i=i+1
        while(l<j):
            if(arr[j]<pivot):
                break;
            j=j-1        
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]          
    if(arr[l]>arr[j]):        
        arr[l],arr[j]=arr[j],arr[l]  
    return j           



arr =[7,9,2,5,88,8,1,23,0]
l=0
h=len(arr)-1
Quicksort(l,h,arr)
print(arr)