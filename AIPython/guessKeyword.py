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
print(LenghtOfAnswer)

def InitialAnswerArray(n):
    arr_string = ''
    # arr_string += '['
    print('[', end='')
    for index in range(LenghtOfAnswer):
        if index < (LenghtOfAnswer - 1):
            arr_string += '\'?\','
        else:
            arr_string += '\'?\''
    # arr_string += ']'
    print(arr_string, end='')
    print(']')
    print("Lives left: " + 9*heart)
    return arr_string
array_string = InitialAnswerArray(LenghtOfAnswer)

def checkWord(word, result):
    index_tmp = 0
    flag = False
    if word == result:
        print('Bingo, You win!!!')
    for index in range(LenghtOfAnswer):
        if word == result[index]:
            # index_tmp.append(index)
            index_tmp = index
            # result[index_tmp] = None
            flag = True
    return index_tmp, flag

def in_game():
    # global lives_remain
    # print(checkWord(guessword, answer))
    # print(array_string)
    # print(array_string.split(','))
    list_arr = array_string.split(',')
    # list_arr = list(array_string)
    # print(list_arr)
    flag = True
    while(flag):
        guessword = input(str('You guess the word is: '))
        ind_, flag = checkWord(guessword, answer)
        if flag:
            # list_arr.index = guessword
            # list_arr = list(map(lambda x: x.replace(array_string[ind_], guessword), array_string))
            list_arr[ind_] = guessword
            pass
        else:
            pass
        print(list_arr)

in_game()