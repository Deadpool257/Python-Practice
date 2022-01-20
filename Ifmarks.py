total_score=0
project=int(input("Enter project marks:"))
external=int(input("Enter external marks:"))
internal=int(input("Enter internal marks:"))
if project>=50 and internal>=50 and external>=50:
    print("Student has passed")
if project<50 and internal<50 and external<50:
    print("Student has failed")
if project>=50 and internal>=50 and external>=50:
    total_score=0.7*project+0.2*external+0.1*internal
    print("Total score is: ",total_score)
if total_score>=90:
    print("Student has acquired A Grade")
if total_score>=75 and total_score<90:
    print("Student has acquired B Grade")
if total_score>=50 and total_score<75:
    print("Student has acquired C Grade")
else:
    if project<50:
        print("Student has failed in project and he acquired a score of ",project)
    if internal<50:
        print("Student has failed in internal and he acquired a score of ",internal)
    if external<50:
        print("Student has failed in external and he acquired a score of ",external)
    
