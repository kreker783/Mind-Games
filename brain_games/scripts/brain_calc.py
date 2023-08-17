import random
from operator import add, mul, sub
import brain_games.cli as cli
import brain_games.logic as logic


def main():
    cli.welcome_user()

    print('What is the result of the expression?')
    game_result = game()

    if game_result:
        cli.game_ending()


def game():
    count = 0
    while count < 3:
        first_number, second_number = random.sample(range(1, 100), 2)
        operation = random.choice([add, sub, mul])
        result = operation(first_number, second_number)

        if operation == add:
            expr = f"{first_number} + {second_number}"
        elif operation == sub:
            expr = f"{first_number} - {second_number}"
        else:
            expr = f"{first_number} * {second_number}"

        validation = logic.validate(result, logic.get_answer(expr))

        if validation:
            count += 1
        else:
            return False
    return True


if __name__ == "__main__":
    main()
