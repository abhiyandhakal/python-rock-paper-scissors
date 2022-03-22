from math import floor
from random import random

# welcome
WELCOME = 'welcome to rock paper scissors'
print('\n' + WELCOME.upper(), '\n')
userScore, compScore = 0, 0
numOfMatches = int(
    input('How many matches do you intend to play? (ideally 3)\n'))


def user_input():
    userInput = str(input('''
    Choose
    'r' for ROCK
    'p' for PAPER
    's' for SCISSORS\n'''))
    return userInput


def read_result():
    f1 = open('user-result.txt', 'r')
    data1 = f1.read()

    f2 = open('comp-result.txt', 'r')
    data2 = f2.read()

    return data1, data2


def write_result(userScore, compScore):
    f1 = open('user-result.txt', 'a')
    f1.write('+' + userScore)
    f1.close()

    f2 = open('comp-result.txt', 'a')
    f2.write('+' + compScore)
    f2.close()


def get_random_num():
    return floor(random()*3)


def convert_num_to_letter(num):
    if num == 0:
        return 'r'
    elif num == 1:
        return 'p'
    elif num == 2:
        return 's'


def convert_letter_to_word(letter):
    if letter == 'r':
        return 'rock'
    elif letter == 'p':
        return 'paper'
    elif letter == 's':
        return 'scissors'


def win_result(u, c):
    print('You have WON as ' + convert_letter_to_word(u).upper() +
          ' beats ' + convert_letter_to_word(c).upper() + '.')
    print('')


def lose_result(u, c):
    print('You have LOST as ' + convert_letter_to_word(u).upper() +
          ' beats ' + convert_letter_to_word(c).upper() + '.')
    print('')


def draw_result(u, c):
    print('It was a DRAW as ' + convert_letter_to_word(u).upper() +
          " doesn't beat " + convert_letter_to_word(c).upper() + '.')
    print('')


def user_and_computer_choice(u, c):
    print('Computer chose ' + convert_letter_to_word(c).upper())
    print('You chose      ' + convert_letter_to_word(u).upper())


def match(userScore, compScore):
    u = user_input()
    c = convert_num_to_letter(get_random_num())

    user_and_computer_choice(u, c)

    # user loses
    if u == 'r' and c == 'p':
        lose_result(u, c)
        compScore += 1
        userScore += 0

    elif u == 'p' and c == 's':
        lose_result(u, c)
        compScore += 1
        userScore += 0

    elif u == 's' and c == 'r':
        lose_result(u, c)
        compScore += 1
        userScore += 0

    # user wins
    elif c == 'r' and u == 'p':
        win_result(u, c)
        compScore += 0
        userScore += 1

    elif c == 'p' and u == 's':
        win_result(u, c)
        compScore += 0
        userScore += 1

    elif c == 's' and u == 'r':
        win_result(u, c)
        compScore += 0
        userScore += 1

    # draw
    else:
        draw_result(u, c)
        compScore += 0
        userScore += 0
    write_result(str(userScore), str(compScore))


def main():
    match(userScore, compScore)
    (data1, data2) = read_result()

    return data1, data2


def win_or_lose(u, c):
    if u > c:
        print('CONGRATULATIONS! YOU WON.')
    elif (u < c):
        print('You lose.')
    else:
        print("It's a draw.")
    print('')


true_or_false = True
while true_or_false:
    for i in range(numOfMatches):
        (data1, data2) = main()
    else:
        true_or_false = False
        print('userScore = ' + data1 + ' = ' + str(eval(data1)))
        print('ComputerScore = ' + data2 + ' = ' + str(eval(data2)))

        win_or_lose(eval(data1), eval(data2))

        # erase previous data
        f1, f2 = open('user-result.txt', 'w'), open('comp-result.txt', 'w')
        f1.write('0')
        f1.close()
        f2.write('0')
        f2.close()
