"""

    Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.

    The Union of the two arrays can be defined as the set containing distinct elements from both arrays.
    If there are repetitions, then only one element occurrence should be there in the union.
"""
print("Enter the number of items you will add in list a:")
i = int(input())
a = []
for i in range(0, i):
    print(f"Enter the {i} element in list a:")
    num = int(input())
    a.append(num)
print("Enter the number of items you will add in list b:")
j = int(input())
b = []
for j in range(0, j):
    print(f"Enter the {j} element in list b:")
    num = int(input())
    b.append(num)

print("List a:", a)
print("List b:", b)

c = a+b
uSet = set(c)
print("The number of elements in the union between these two arrays:", len(uSet))