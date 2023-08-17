from random import sample, choice
from operator import add, mul, sub
import brain_games.engine.logic as logic


def game():
    count = 0
    while count < 3:
        first_number, second_number = sample(range(1, 100), 2)
        operation = choice([add, sub, mul])
        result = operation(first_number, second_number)

        expression = get_expression(first_number, second_number, operation)

        validation = logic.validate(result, logic.get_answer(expression))

        if validation:
            count += 1
        else:
            return False
    return True


def get_expression(first_number, second_number, op):
    if op == add:
        expr = f"{first_number} + {second_number}"
    elif op == sub:
        expr = f"{first_number} - {second_number}"
    else:
        expr = f"{first_number} * {second_number}"

    return expr
