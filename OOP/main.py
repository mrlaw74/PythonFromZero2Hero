class Person:
    power = 50
    def __init__(self, name, age, male):
        self.name = name
        self.age = age
        self.male = male
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self, age):
        self.age = age
    def getAge(self, age):
        return self.age
    def setMale(self, male):
        self.male
    def getMale(self):
        return self.male
    def setID(self, ID):
        self.ID = ID
    def getID(self):
        return self.ID
    def setSchool(self, school):
        self.school = school
    def getSchool(self):
        return self.school
    def __del__(self):
        print("Ham bi huy")
        del self

class Student(Person):
    ID = "1712085"
    school = "Bach Khoa"

person1 = Person("Luat", 23, True)
print(person1.name)
print(person1.getName())
student1 = Student("Luat2", 24, True)
print(student1.getID())
print(student1.ID)

student1.power = 40
print(Person.power)
print(student1.power)

Person.power = 40
print(Person.power)
print(student1.power)
# student1 = Student(person1, 3120, "ABC")
# print(student1.school)
# print(student1.getSchool())


