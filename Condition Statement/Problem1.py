"""
Given a positive integer x. Your task is to check,
if it is even or odd
(Any number that gives zero as remainder when divided by 2 is an even number)

"""

a = int(input())
print(f"{a} is Even" if a % 2 == 0 else f"{a} is Odd")

# We use the modulo operator (%) to find the remainder when dividing 'a' by 2.
# If the remainder is 0, the number is even; otherwise, it's odd.

"""
>>> checkOddEven(10)
Even

>>> checkOddEven(-9)

>>> checkOddEven(6.4)
Exceptional error,  float always comes out as odd so we are only taking int inputs

"""
