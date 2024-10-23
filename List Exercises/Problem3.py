"""
    Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.

    Intersection of two arrays is said to be elements that are common in both arrays.
    The intersection should not count duplicate elements.
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

c = set(a).intersection(set(b))
if not c:
    print(f"The intersection of both arrays is 0, there's no common element in between {a} and {b}")
else:
    print(f"The intersection in between {a} and {b} is:",sorted(list(c)))
    
    