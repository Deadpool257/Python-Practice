count=0
i=int(input("Enter the value:"))
list1=[23,45,56,23,90,77]
for j in list1:
    if i==j:
        count=count+1
if count>1:
    print(count)
elif count==1:
    print("one occurence")
else:
    print("Invalid Input")