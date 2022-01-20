unit=int(input("Enter the number of units:"))
if unit<=50:
    bill=0.75*unit
    total_bill=bill*0.1
    print("Bill and total_bill are:",bill,total_bill)
elif unit>50 and unit<=150:
    bill=((50*0.75)+(unit-50)*2.10)
    total_bill=bill*0.1
    print("Bill and total bill are:",bill,total_bill)
elif unit>150 and unit<=250:
    bill=((50*0.75)+(100*2.10)+(unit-150)*2.50)
    total_bill=bill*0.1
    print("Bill and total_bill are:",bill, total_bill)
else:
    bill=((50*0.75)+(100*2.10)+(100*2.50)+(unit-250)*2.80)
    total_bill=bill*0.1
    print("Bill and total_bill are:",bill,total_bill)