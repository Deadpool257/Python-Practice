number=int(input("Enter a value:"))
for i in range(1,number):
    if number%i==0:
        print(i,end=",")
        i=i+i
    if number==i:
        print("\n")
        print("Given number is perfect")
    