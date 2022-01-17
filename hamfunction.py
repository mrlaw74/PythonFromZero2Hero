from typing import final


def tong2so(a,b):
    return a+b
print("tong 2 so la " + str(tong2so(2,3)))

def sumnhieuso(*num):
    temp = 0
    for i in num:
        temp += i
    return temp
print("Tong nhieu so la " + str(sumnhieuso(1,2,3,4,5,6,7,8,9,10)))

def division(a,b):
    return a/b
try :
    print("Ket qua chia la " + str(division(10,0)))
except (ZeroDivisionError, RuntimeError):
    print("Khong the chia cho 0")
try:
    subtotal = input("Enter total before tax:")
    tax = 0.08 * subtotal
    print("tax on", subtotal, "is:", tax)
except (TypeError):
    print("Invalid input, error at Type error")
finally :
    print("End of try except program")
