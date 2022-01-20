y=0
n=int(input("Enter the value:"))
for i in range(1,n+1,1):
    if n%i==0:
        y+=1
print("n.o of factors are:",y)