class SoNguyenTo():
    def __init__(self, number):
        self.number = number
        if self.isSoNguyenTo():
            pass
        else:
            del self.number
    def isSoNguyenTo(self):
        for i in range(2, self.number):
            if(self.number % i == 0):
                return False
        return True
    def nextSoNguyenTo(self):
        for self.number in range(self.number+1, self.number*2):
            try:
                if(self.number.isSoNguyenTo()):
                    return self.number
                    break
                else:
                    pass
            except:
                print("So Nguyen To object has no attribute 'number' so we can not print it")
            
number1 = SoNguyenTo(int(input("Input first number: ")))
# print(number1.number)
try:
    print(number1.number)
    print(number1.isSoNguyenTo())
    print(number1.nextSoNguyenTo())
except:
    print("So Nguyen To object has no attribute 'number' so we can not print it")
