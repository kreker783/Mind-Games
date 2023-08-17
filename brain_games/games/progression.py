from random import randint, choice
import brain_games.engine.logic as logic


def game():
    count = 0
    while count < 3:
        start_number = randint(1, 100)
        difference = randint(1, 10)

        result, progression = pick_element(get_progression(start_number, difference))

        validation = logic.validate(result, logic.get_answer(progression))

        if validation:
            count += 1
        else:
            return False
    return True


def get_progression(a, d, n=9):
    result = [a]
    for i in range(1, n+1):
        a = a + d
        result.append(a)
    return result


def pick_element(progression):
    element = choice(progression)
    index = progression.index(element)
    progression[index] = '..'
    return element, " ".join(str(i) for i in progression)
