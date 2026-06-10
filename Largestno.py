largest = None

while True:
    num = input("Enter number (or 'done'): ")
    
    if num == "done":
        break
    
    num = int(num)
    
    if largest is None or num > largest:
        largest = num

print("Largest:", largest)
