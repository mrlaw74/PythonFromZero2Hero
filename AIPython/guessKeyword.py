# Game guess keyword
import random
string_random = ['one', 'two', 'three', 'four',
                 'six', 'seven', 'eight', 'football',
                 'badminton', 'goal', 'family', 'father']
lives_remain = 9
heart = "\u2764\uFE0F "
answer = random.choice(string_random)
print(answer)
LenghtOfAnswer = len(answer)
check = 0
# print(LenghtOfAnswer)

def InitialAnswerArray(n):
    arr_string = ''
    print('[', end='')
    for index in range(LenghtOfAnswer):
        if index < (LenghtOfAnswer - 1):
            arr_string += '\'?\','
        else:
            arr_string += '\'?\''
    print(arr_string, end='')
    print(']')
    print("Lives left: " + 9*heart)
    return arr_string
array_string = InitialAnswerArray(LenghtOfAnswer)

def checkWord(word, result):
    global check
    index_tmp = []
    flag = False
    if word == result:
        print('Bingo, You win!!!')
        quit()
    for index in range(LenghtOfAnswer):
        if word == result[index]:
            index_tmp.append(index)
            flag = True
    check += len(index_tmp)
    return index_tmp, flag

def checkWin():
    global check
    global LenghtOfAnswer
    if check == LenghtOfAnswer:
        print('Bingo, You win!!!')
        quit()
    
def in_game():
    global lives_remain
    list_arr = array_string.split(',')
    flag = True
    while(lives_remain != 0):
        checkWin()
        guessword = input(str('You guess the word is: '))
        ind_, flag = checkWord(guessword, answer)
        if flag:
            for index in ind_:
                list_arr[index] = guessword
            print("Good job bro!")
        else:
            lives_remain -= 1
            if (lives_remain > 0):
                print("Lives left: " + lives_remain*heart)
            else:
                print ("Game over")
                quit()
        print(list_arr)

in_game()