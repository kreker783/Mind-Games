from random import randint
import brain_games.engine.logic as logic


def game():
    count = 0
    while count < 3:
        number = randint(1, 100)
        result = get_result(number)

        validation = logic.validate(result, logic.get_answer(number))

        if validation:
            count += 1
        else:
            return False
    return True


def get_result(number):
    return "yes" if number % 2 == 0 else "no"
