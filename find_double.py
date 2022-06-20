from unittest import result


lis = ['a', 'b', 'd', 'a', 'c', 'd', 'b', 'k', 123, 23, 123, 'k']
print(lis.count('a'))
print(lis.count('a'))
print(lis[1])
result = []
for i in range(len(lis)):
    tmp = lis.count(lis[i])
    if tmp >= 2:
        result.append(lis[i])
result = set(result)
print(result)
