#WAP to print sum of even numbers and sum of odd numbers between 1-n
esum=0
osum=0
n=int(input("Enter a value:"))
for i in range(1,1+n):
    if i%2==0:
        esum=esum+i
    else:
        osum=osum+i
print("Sum of even numbers:",esum)
print("Sum of odd numbers:",osum)