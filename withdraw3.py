bal1=0
bal2=0
bal3=0
bal4=0
bal5=0
amount=int(input("Enter the number of notes:"))
if amount%10==0:
    if amount>=200:
        a=amount//200
        amount=amount-(a*200)
        print("200 rupees notes are:",a)
    if amount>=100:
        b=amount//100
        amount=amount-(b*100)
        print("100 rupees notes are:",b)
    if amount>=50:
        c=amount//50
        amount=amount-(c*50)
        print("50 rupees notes are:",c)
    if amount>=20:
        d=amount//20
        amount=amount-(d*20)
        print("20 rupees notes are:",d)
    if amount>=10:
        e=amount//10
        amount=amount-(e*10)
        print("10 rupees notes are:",e)
else:
    print("Invalid amount")
                