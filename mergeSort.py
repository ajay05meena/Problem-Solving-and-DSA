def mergeSort(A,l,h):
    a=[x for x in A] 
    if(l<h):
        mid=(l+h)//2
        mergeSort(a,l,mid)
        mergeSort(a,mid+1,h)
        merge(a,l,mid,h)
        return a
    
def merge(a,l,mid,h):
    print(a,l,mid,h)
    MergingArray=[x for x in a]  
    k=0
    i=l
    j=mid
    while(k<h):
        if(j>=h):
            a[k]=MergingArray[i]
            i=i+1
            k=k+1
            continue
        if(i>=mid):
            a[k]=MergingArray[j]
            j=j+1
            k=k+1
            continue
        if(MergingArray[i]<=MergingArray[j]):
            a[k]=MergingArray[i]
            i=i+1
            k=k+1
            continue
        if(MergingArray[i]>MergingArray[j]):
            a[k]=MergingArray[j]
            j=j+1
            k=k+1 
            continue     


if __name__ == '__main__':
    testCases = [[9,34,4,24,1]]
    results =   [[1,4,9,24,34]]
    for i in range(len(testCases)):
        if mergeSort(testCases[i],0,len(testCases[i])-1) == results[i]:
            print("Test Succeed ",i)
        else:
            print("Test Failed ", i)