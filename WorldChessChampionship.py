def Winner(X,Str):
        Carlsen=0
        Chef=0
        for x in range(0,len(Str)):
            if Str[x]=="C":
                Carlsen=Carlsen+2
            if Str[x]=="N":
                Chef=Chef+2
            if Str[x]=="D":
                Carlsen=Carlsen+1 
                Chef=Chef+1      
        
        if Carlsen>Chef:
            print(60*X)
        elif Carlsen==Chef:
            print(55*X)
        else:
            print(40*X)        





if __name__=="__main__":
     try:
            t=int(input())
            for i in range(t):
                X=int(input())
                Str=input()
                Winner(X,Str)
     except:
        pass        