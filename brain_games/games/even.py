from random import randint
import brain_games.engine.cli as cli
import brain_games.engine.logic as logic


def main():
    cli.welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_result = game()

    if game_result:
        cli.game_ending()


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


if __name__ == "__main__":
    main()