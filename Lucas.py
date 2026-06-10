def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

n = int(input("Enter number of terms: "))

for i in range(n):
    print(lucas(i), end=" ")
