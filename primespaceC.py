count=0
number=int(input("Enter the value:"))
for i in range(1,number):
    if number%i==0:
        count=count+1
if count>1:
    print("Entered number is not a prime number")
else:
    print("Entered number is a prime number")

