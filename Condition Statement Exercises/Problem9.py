"""

    You are given a number n. The number n can be negative or positive.
    If n is negative, print numbers from n to 0 by adding 1 to n in the neg function.
    If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.
    
    """


def pos(n):
    # Write the code
    while (n >= 0):
        print(n-1, end=" ")
        n -= 1
        if n == 0:
            break


def neg(n):
    # Write the code
    while (n <= 0):
        print(n, end=" ")
        n += 1


N = int(input())

if (N > 0):
    pos(N)
elif (N < 0):
    neg(N)
else:
    print("It's Zero")
