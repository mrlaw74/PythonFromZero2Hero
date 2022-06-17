def super_function(*asd):
    print(*asd)
    return sum(asd)
print(super_function(1, 2, 3, 4, 5))