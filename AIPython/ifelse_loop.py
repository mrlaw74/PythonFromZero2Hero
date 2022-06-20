# Input: a and b
# if a = 0, y = b^2
# if a = K, y = square b

from math import sqrt


def square(a,b):
    result = 0
    if a == 0:
        result = b*b
    # elif a == K:
    #     result = sqrt(b)
    else:
        result = sqrt(b)
    return result    
a = int(input('a = '))
b = int(input('b = '))
# K = int(input('K = '))
print(square(a,b))
