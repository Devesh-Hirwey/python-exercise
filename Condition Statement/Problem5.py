"""
    You are given a number N, you need to print its multiplication table.
    """


# in is a membership operator that is true if something is a member of sequence
N = int(input())
for i in range(1,11):
    print(f"{N} * {i} =", i * N)