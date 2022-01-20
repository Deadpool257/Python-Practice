number=int(input("Enter the value:"))
for i in range(1,number):
    if(number%i==0 and i!=1):
        print("Given value is not a prime number")
        break
    else:
        print("Entered number is a prime number")
        break