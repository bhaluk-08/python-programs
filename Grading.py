attendance = float(input("Enter attendance %: "))
marks = int(input("Enter marks: "))

if attendance < 50:
    print("Detained (Not eligible)")
else:
    print("Eligible for exam")
    
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"
    
    print("Grade:", grade)
    
    if attendance >= 90 and marks >= 90:
        print("Distinction Certificate")
