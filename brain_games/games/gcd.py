from random import sample
from math import gcd
import brain_games.engine.logic as logic


def game():
    count = 0
    while count < 3:
        first_number, second_number = sample(range(1, 100), 2)
        result = get_result(first_number, second_number)

        answer = logic.get_answer(str(f"{first_number} {second_number}"))

        validation = logic.validate(result, answer)

        if validation:
            count += 1
        else:
            return False
    return True


def get_result(x, y):
    return gcd(x, y)
