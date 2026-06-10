while True:
    name = input("Enter employee name (or exit): ")
    
    if name == "exit":
        break
    
    salary = float(input("Enter salary: "))
    
    if salary < 20000:
        print("Low salary - continue")
        continue
    
    bonus = salary * 0.1
    total = salary + bonus
    
    print("Total Salary:", total)
