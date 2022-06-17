n=int(input("enter the number"))
i=1
while i<=n:
    k=1
    while k<i:
        print(" ",end="")
        k=k+1
    j=0
    while j<=n-i:
        j=j+1
        print(j,end="")
    print()
    i=i+1       