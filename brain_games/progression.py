import random
from brain_games.game_logic import greeting
from brain_games.game_logic import check


def progression():
    name = greeting()
    print('What number is missing in the progression?')
    counter = 0
    while counter != 3:
        start = random.randint(1, 50)  # Начальное значение
        step = random.randint(1, 10)   # Шаг прогрессии
        n = random.randint(5, 10)  # Длина прогрессии
        i = random.randint(0, n - 1)  # Индекс числа, которое будем прятать
        progression = list(range(start, start + step * n, step))
        # print(progression) # Для отладки
        progression_copy = progression[:]
        progression_copy[i] = '..'
        print(f'Question: {" ".join(map(str, progression_copy))}')
        right_answer = progression[i]
        counter = check(right_answer, counter)
        if counter == 0:
            print(f"Let's try again, {name}!")
    print('Congratulations, ' + name + '!')
