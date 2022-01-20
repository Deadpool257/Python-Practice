amount=int(input("Enter the amount:"))
if amount>=500:
    a=amount//500
    bal=amount-(500*a)
    if bal>=200:
        b=bal//200
        bal2=bal-(200*b)
        if bal2>=100:
            c=bal2//100
            print("500 rupees notes are:",a)
            print("200 rupees notes are:",b)
            print("100 rupees notes are:",c)
else:
    print("Invalid")
        