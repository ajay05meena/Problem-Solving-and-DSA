arr1={}
for i in range(0,26):
    arr1[i]=chr(i+65)

arr={v:k for k,v in arr1.items()}
t=input("Give plaintext string : ")
Plaintext=list(t)
key=int(input("Give key value : "))
for x in range(0,len(Plaintext)):
    temp=arr[Plaintext[x]]
    Plaintext[x]=arr1[(temp+key)%26]

Ciphertext=''.join(Plaintext)
print("Ciphertext for Paintext : "+t+" which is : "+Ciphertext)