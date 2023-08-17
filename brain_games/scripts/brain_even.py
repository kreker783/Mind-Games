import brain_games.engine.cli as cli
from brain_games.games.even import game


def main():
    cli.welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_result = game()

    if game_result:
        cli.game_ending()


if __name__ == "__main__":
    main()
