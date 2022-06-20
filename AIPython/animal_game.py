# Initialize constant value, initial value of variables
score = 0
incorrect_try_again = 1
question = {'Which mammal is known to have the most powerful bite in the world?': 'Hippopotamus',
            'Which animal is known to spend 90% of its day, sleeping?' : 'Koalas',
            'What color is the tongue of a giraffe?' : 'Purple',
            'Which animal’s stripes are on their skin as well as their fur?' : 'Tiger',
            ' Which animal’s poop is known to take the shape of cubes?': 'Wombat',
            'Under their white fur, what color is a polar bear’s skin?' : 'Black'
            }
class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def intro_funtion():
    print("Hello, Welcome to the Animal Game!")
    print("You have to answer the animal that I will ask you!")
    print("If you answer correctly, you will get a point!")
    print("Oherwise, you will not any point more!")
    print("Good luck!")

def ask_question():
    answer  = ''
    try_times = 0
    global score
    A = list(question.keys())
    B = list(question.values())
    for index in range(len(question) - 1):
        print(A[index])
        answer = input("Your answer: ").casefold()
        while (answer != B[index].casefold()) and (try_times < incorrect_try_again):
            print("Not correct!, try again:")
            try_times += 1
            print(A[index])
            answer = input("Your answer: ").casefold()
        try_times = 0
        if answer == B[index].casefold():
            print("Correct!")
            score += 1
        else:
            print("Unfortunately, you are wrong!\nNext question!!!")
    print("You have finished the game! Your score is: ", score)
    # answer = input(str("Which mammal is known to have the most powerful bite in the world? "))
    
def main():
    intro_funtion()
    ask_question()
if __name__ == '__main__':
    main()