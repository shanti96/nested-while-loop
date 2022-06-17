n=int(input("enter the number"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k=k+1
    j=0
    while j<i:
        print(i-j,end="")
        j=j+1
    p=1
    while p<i:
        p=p+1
        print(p,end="")
    print()
    i=i+1    