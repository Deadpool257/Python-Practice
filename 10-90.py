count=9
r=91
for i in range(5):
    for j in range(5):
        if i%2==0:
            count=count+1
            print(count,end=" ")
        else:
            r=r-1
            print(r,end=" ")
    print()