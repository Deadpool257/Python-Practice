fmax=0
smax=0
for i in range(6):
    n=int(input("Enter the value:"))
    if fmax<n:
        smax=fmax
        fmax=n
print("Maximum value is:",fmax)
print("Second Maximum value is:",smax)