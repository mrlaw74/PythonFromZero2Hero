class SoHoc():
    def __init__(self, number1, number2):
        self.number1, self.number2 = number1, number2
    def setNumber1(self, number1):
        self.number1 = number1
    def setNumber2(self, number2):
        self.number2 = number2
    def getNumber1(self):
        return self.number1
    def getNumber2(self):
        return self.number2
    def inputInfo(self):
        self.number1 = int(input("Input first number: "))
        self.number2 = int(input("Input second number: "))
    def printInfo(self):
        print(f"The first number is: {self.number1}")
        print(f"The second number is: {self.number2}")
    def addition(self):
        return self.number1 + self.number2
    def subtract(self):
        return self.number1 - self.number2
    def multi(self):
        return self.number1 * self.number2
    def divition(self):
        return self.number1 / self.number2

class NhanVien():
    def __init__(self, name, age, address, salary, workinghour):
        self.name, self.age, self.address, self.salary, self.workinghour = name, age, address, salary, workinghour
    def inputInfo(self):
        self.name           = str(input("Name: "))
        self.age            = int(input("Age: "))
        self.address        = str(input("Address: "))
        self.salary         = int(input("Salary: "))
        self.workinghour    = int(input("working hour: "))
    def printInfo(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Salary: {self.salary}")
        print(f"working hour: {self.workinghour}")
    def tinhThuong(self):
        if(self.workinghour >= 200):
            thuong = self.salary*0.2
        elif(self.workinghour >= 100 and self.workinghour < 200):
            thuong = self.salary*0.1
        else:
            thuong = 0
        return thuong

class Student():
    def __init__(self, ID, avg_score, age, group):
        self.ID, self.avg_score, self.age, self.group = ID, avg_score, age, group
    def inputInfo(self):
        self.ID         = str(input("ID: "))
        self.avg_score  = float(input("Average score: "))
        self.age        = int(input("Age: "))
        self.group      = str(input("Group: "))
    def printInfo(self):
        print(f"ID: {self.ID}")
        print(f"Average score: {self.avg_score}")
        print(f"Age: {self.age}")
        print(f"Group: {self.group}")
    def HocBong(self):
        if self.avg_score >= 8:
            print(f"{self.ID} duoc hoc bong =)).")
        else:
            print(f"{self.ID} khong duoc hoc bong =)).")
            