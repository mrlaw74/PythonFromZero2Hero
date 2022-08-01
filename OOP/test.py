def checkNguyenTo(num):
    if num == 1:
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True
def nextNguyenTo(num):
    for i in range(num+1, num*2):
        if checkNguyenTo(i):
            return i
            break
print(nextNguyenTo(int(input("Input number: "))))