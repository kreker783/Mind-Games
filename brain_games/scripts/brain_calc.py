import brain_games.engine.cli as cli
from brain_games.games.calc import game


def main():
    cli.welcome_user()

    print('What is the result of the expression?')
    game_result = game()

    if game_result:
        cli.game_ending()


if __name__ == "__main__":
    main()
