def Horses(x,a):
    a.sort()
    min=abs(a[0]-a[1])
    for i in range(1,x-1):
        t=abs(a[i]-a[i+1])
        if(t<min):
            min=t
    print(min)
    

            
            




if __name__=="__main__":
    try:
        t=int(input())
        for i in range(t):
            x=int(input())
            a=list(map(int,input().split()))
            Horses(x,a) 


    except:
        pass    