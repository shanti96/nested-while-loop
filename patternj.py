a=int(input("enter number"))
i=1
while i<=a:
    k=a
    while k>i:
        print(" ",end="")
        k=k-1
    j=0
    while j<i:
        print(i-j,end="")
        j=j+1
    print()
    i=i+1       