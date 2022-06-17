from enum import Flag
import re
# String method in Python
# 1. Length of a string
# string = 'hello World'
# print(len(string))

# print(re.findall('o', string))
flag = False
fp = open('./nguyen.txt', 'r')
with open('./nguyen.txt') as fp:
    for line in fp:
        x = re.search(r".*username\:\s(.*)\sm.*", line)
        if x is not None:
            # print(x.group(1))
            flag = True  
        if flag:
            flag = False
            print('Ok')
            y = re.search(r"\bTC_\d{2}_\d{2}_\d{3}\b", line)
            if y is not None:
                print(y.group(1))
                break
fp.close()
# x = re.search(r".*username\:\s(.*)\sm.*", txt)
# y = re.search(r"\bTC_\d{2}_\d{2}_\d{3}\b", txt)
# # print(x.span())
# # print(x.string)
# # a = x.group(2)
# # print(x.group())
# print(x.group(1))
# if x.group(1) is "Stack":
#     print('Found Stack')
#     print(x.group(1))
#     print(type(x.group(1)))
#     y = re.search(r"\bTC_\d{2}_\d{2}_\d{3}\b", txt)
#     if y is not None:
#         print(y.group(1))
#     else:
#         pass
# else:
#     print('Not Found Stack')
# # print(a)
