n=int(input("Enter a number\n"))
a=1
b=1
print(a,b,end=" ")
for x in range(0,n,1):
    c=a+b
    print(c, end=" ")
    a=b
    b=c

