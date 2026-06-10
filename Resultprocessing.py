def input_marks():
    marks = []
    for i in range(3):
        m = int(input(f"Enter mark {i+1}: "))
        marks.append(m)
    return marks

def total(marks):
    return sum(marks)

def average(marks):
    return sum(marks)/len(marks)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

# Main
marks = input_marks()
tot = total(marks)
avg = average(marks)

print("Total:", tot)
print("Average:", avg)
print("Grade:", grade(avg))
