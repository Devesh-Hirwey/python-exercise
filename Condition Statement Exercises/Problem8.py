"""
    Given a positive integer x,
    the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).
    """

x = int(input())
i = 1
while (i ** 2 <= x):
    print(i ** 2, end = " ")
    i += 1
