n=int(input("enter the number"))
i=1
p=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=p:
        print(i,end="")
        j=j+1
    print() 
    p=p+2
    i=i+1   