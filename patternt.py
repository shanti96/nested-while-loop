n=int(input("enter the number"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
        p=0
        while p<1:
            print(" ",end="")
            p=p+1
    print()
    i=i+1    