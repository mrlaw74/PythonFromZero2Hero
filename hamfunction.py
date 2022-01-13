def tong2so(a,b):
    return a+b
print("tong 2 so la " + str(tong2so(2,3)))

def sumnhieuso(*num):
    temp = 0
    for i in num:
        temp += i
    return temp
print("Tong nhieu so la " + str(sumnhieuso(1,2,3,4,5,6,7,8,9,10)))