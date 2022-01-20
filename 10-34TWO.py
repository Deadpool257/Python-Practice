a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
d=int(input("Enter d value:"))
for i in range(a,b,c):
    for j in range(d):
        print(i,end=" ")
        i=i+1
    print()