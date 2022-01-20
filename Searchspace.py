count=0
list1=[23,56,44,78,23,44]
j=int(input("Enter a value"))
for i in list1:
    if i==j:
        count=count+1
if (count!=0):
    print(count)
else:
    print("It is not in the list")