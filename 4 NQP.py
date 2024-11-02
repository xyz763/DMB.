def is_consistent(queens, n):
    return all(queens[i] != queens[n] and abs(queens[i] - queens[n]) != n - i for i in range(n))

def print_queens(queens):
    for i in queens:
        print(" ".join("Q" if j == i else "*" for j in range(len(queens))))
    print()

def enumerate_queens(queens, k):
    if k == len(queens):
        print_queens(queens)
    else:
        for i in range(len(queens)):
            queens[k] = i
            if is_consistent(queens, k):
                enumerate_queens(queens, k + 1)

n = int(input("Enter number of queens: ") or 8)
enumerate_queens([0] * n, 0)
