import random
from brain_games.game_logic import greeting
from brain_games.game_logic import check


def is_prime(n):
    if n <= 3:
        return 'yes'
    if n % 2 == 0 or n % 3 == 0:
        return 'no'
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 'no'
        i += 6
    return 'yes'


def prime():
    name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter != 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        right_answer = is_prime(random_number)
        counter = check(right_answer, counter)
        if counter == 0:
            print(f"Let's try again, {name}!")
    print('Congratulations, ' + name + '!')
