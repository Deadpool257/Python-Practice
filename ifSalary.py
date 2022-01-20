salary=int(input("Enter the Basic Salary:"))
if salary>0:
    if salary<10000:
        da=0.7*salary
        hra=0.65*salary
        gross_salary=salary+hra+da
        print("Gross Salary",gross_salary)
    elif salary>=10000 and salary<=20000:
        da=0.75*salary
        hra=0.73*salary
        gross_salary=salary+hra+da
        print("GrossSalary",gross_salary)
    elif salary>20000:
        da=0.80*salary
        hra=0.76*salary
        gross_salary=salary+hra+da
        print("GrossSalary",gross_salary)
else:
    print("Invalid Input")