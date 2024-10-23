"""
    Given an array arr. Your task is to find the minimum and maximum elements in the array.

    Note: Return an array that contains two elements the first one will be
    a minimum element and the second will be a maximum of an array.
    
"""
# we can easily solve this using min, max prebuilt functions but in this code we won't be using that...

i = int(input())
list = []
for _ in range(0, i):
    num = int(input())
    list.append(num)
print(list)

list.sort()
print(list[0], " ", list[-1])