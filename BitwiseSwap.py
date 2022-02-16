if __name__=="__main__":
    try:
        t=int(input())
        for i in range(t):
            x=int(input())
            a=list(map(int,input().split())) 
            i=0
            while(i<x-1):
                    store=i
                    k=i
                    for j in range(i+1,x):
                        Andvalue=a[i]&a[j]
                        if(Andvalue==0):
                            continue
                        if(Andvalue>0 and a[i]>a[j]):
                            if(a[store]>a[j]):
                                store=j
                    if(store>i):            
                        a[i],a[store]=a[store],a[i]
                        i=k
                    else:
                        i=i+1          
            count=0            
            for i in range(0,x-1)  :          
              if(a[i]>a[i+1]):
                  count=count+1

            if(count==0):
                print("Yes")
            else:
                print("No")           
                   
                 


    except:
        pass   