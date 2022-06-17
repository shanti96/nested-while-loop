n=int(input("enter the row line"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
        f=j
        while f<i:
            print(" ",end=" ")
            f=f+1
        j=f  
    print()
    i=i+2
a=1
while a<=n:  
    b=0
    while b<=a:
        print(" ",end="")
        b=b+1
    c=1
    while c<n-a:
        print("*",end=" ")
        c=c+1  
        d=c
        while d<(n-a)-1:
            print(" ",end=" ")
            d=d+1
        c=d           
    print()
    a=a+2             