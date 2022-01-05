#Calculating percentage of class attendance
working_days = int(input("Enter no_of working days : "))
absent_days = float(input("Enter no_of absent days : "))
if working_days<=0 or absent_days>working_days or working_days>365 :
    print("You had entered incorrect data")
else :
    present_days = working_days-absent_days
    attend_percent = (present_days/working_days)*100
    print("\n\t No.of Working days : ",working_days)
    print("\t No.of Absent days : ",absent_days)
    print("\t No.of Present days : ",present_days)
    print("\t----------------------------------------------")
    print("\t Percentage of class attendance : ",attend_percent)
    print("\t----------------------------------------------")
    if attend_percent >=75 :
        print("***You are good in class attendance, you can write the exam***\n")
    else :
        print("***Your class attendance is not enough to write the exam***")
        
