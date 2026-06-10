def check_num(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

num = int(input("Enter number: "))
check_num(num)
