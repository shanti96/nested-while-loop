n=int(input("enter the number"))
i=1
p=1
while i<n:
    k=1
    while k<n-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=p:
        print("*",end="")
        j=j+1
    print()
    i=i+1
    p=p+2