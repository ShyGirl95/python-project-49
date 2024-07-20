import random
from brain_games.game_logic import greeting
from brain_games.game_logic import check
from brain_games.game_logic import prime_factors
from functools import reduce
from operator import mul
from collections import Counter


def gcd():
    name = greeting()
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter != 3:
        random_number_1 = random.randint(1, 100)
        random_number_2 = random.randint(1, 100)
        print(f'Question: {random_number_1} {random_number_2}')
        prime_factors_1 = prime_factors(random_number_1)
        prime_factors_2 = prime_factors(random_number_2)
        counter_1 = Counter(prime_factors_1)
        counter_2 = Counter(prime_factors_2)
        # Для отладки
        # print(prime_factors(random_number_1))
        # print(prime_factors(random_number_2))
        intersection = []
        for i in counter_1:
            if i in counter_2:
                min_count = min(counter_1[i], counter_2[i])
                intersection.extend([i] * min_count)
        # Для отладки
        # print(intersection)
        if len(intersection) == 0:
            right_answer = 1
        else:
            right_answer = reduce(mul, intersection)
        counter = check(right_answer, counter)
        if counter == 0:
            print(f"Let's try again, {name}!")
    print('Congratulations, ' + name + '!')
