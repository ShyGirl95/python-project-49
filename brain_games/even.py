import random
from brain_games.game_logic import greeting
from brain_games.game_logic import check


def even():
    name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter != 3:
        random_number = random.randint(1, 100)
        print('Question: ' + str(random_number))
        if random_number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        counter = check(right_answer, counter)
        if counter == 0:
            print(f"Let's try again, {name}!")
    print('Congratulations, ' + name + '!')
