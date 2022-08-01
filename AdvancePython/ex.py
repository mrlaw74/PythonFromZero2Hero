from functools import reduce

# # Use map to print the square of each numbers rounded
# # to three decimal places
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# result_map = list(map(lambda x: round(x*x, 3), my_floats ))
# print(result_map)

# # Use filter to print only the names that are less than
# # or equal to seven letters
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# result_filter = list(filter(lambda x:len(x)<=7, my_names))
# print(result_filter)

# # Use reduce to print the product of these numbers
# my_numbers = [4, 6, 9, 23, 5]
# result_reduce = reduce(lambda a, b:a*b, my_numbers)
# print(result_reduce)
a = ["a", "b", "c", "a"]
b = set(a)
result = []
for item in b:
    print (a.count(item))
print(b)
