def Helium3(A,B,X,Y):
    s=A*B
    k=X*Y
    if(s<=k):
        print("Yes")
    if(s>k):
        print("No")            


try : 
    t=int(input())
    for i in range(t):
        A,B,X,Y=map(int,input().split(" "))
        Helium3(A,B,X,Y)
except:
  pass
    
    