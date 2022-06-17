a=int(input("enter number"))
b=1
while b<=a:
    c=a
    while c>=b:
        print("",end=" ")
        c=c-1
    d=1
    while d<b:
        print("*",end=" ")
        d=d+1
    print()
    b=b+1
e=a
b=1
while b<e:
    d=1
    while d<=b:
        print(" ",end="")
        d=d+1
    c=e
    while c>b:
        print("*",end=" ")
        c=c-1
    print()
    b=b+1