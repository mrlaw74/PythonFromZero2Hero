from abc import abstractmethod


class PlayerCharacter():
    def __init__(self, name, age,):
        self._name, self._age = name, age
        # self.speak = speak
    def run(self):
        print("run")
    def speak(self):
        print(f"my name is {self._name}, and I am {self._age} years old")

player1 = PlayerCharacter("Tom", 20)

# print(player1.name)
player1.speak = "Hello"
print(player1.speak)
print(player1.speak())