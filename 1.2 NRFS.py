def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Enter number of terms: "))
print("Fibonacci sequence:")
[print(fibonacci(i)) for i in range(n)]