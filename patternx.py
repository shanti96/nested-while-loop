n=int(input("enter the number"))
i=1
k=65
while i<=n:
    j=1
    while j<=i:
        print(chr(k),end="")
        j=j+1
    print()
    k=k+1
    i=i+1    
