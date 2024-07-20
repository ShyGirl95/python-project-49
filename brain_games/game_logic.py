import prompt


def greeting():
    print("Welcome to the Brain Games!")
    name = (prompt.string('May I have your name? ')).capitalize()
    print('Hello, ' + name + '!')
    return name


def check(right_answer, counter):
    while True:
        answer_user = input('Your answer: ')
        if type(right_answer) is int:
            answer_user = int(answer_user)
        if answer_user == right_answer:
            counter += 1
            print('Correct!')
            break
        else:
            counter = 0
            print(f"'{answer_user}' is wrong answer ;"
                  f"(. Correct answer was '{right_answer}'")
            break
    return counter


def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors
