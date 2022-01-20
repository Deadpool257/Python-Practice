count=0
number=int(input("Enter a value:"))
for i in range(1,number):
    if i%i==0 and i!=1:
        print(i)
        continue
    