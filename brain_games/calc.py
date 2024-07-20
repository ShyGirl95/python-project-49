import random
from brain_games.game_logic import greeting
from brain_games.game_logic import check


def calc():
    name = greeting()
    print('What is the result of the expression?')
    counter = 0
    while counter != 3:
        operators = ('+', '-', '*')
        random_operator = random.choice(operators)
        random_number_1 = random.randint(1, 100)
        random_number_2 = random.randint(1, 100)
        print(f'Question: {random_number_1} {random_operator} '
              f'{random_number_2}')
        if random_operator == '+':
            right_answer = random_number_1 + random_number_2
        elif random_operator == '-':
            right_answer = random_number_1 - random_number_2
        elif random_operator == '*':
            right_answer = random_number_1 * random_number_2
        # Для отладки
        # print(right_answer)
        counter = check(right_answer, counter)
        if counter == 0:
            print(f"Let's try again, {name}!")
    print('Congratulations, ' + name + '!')
