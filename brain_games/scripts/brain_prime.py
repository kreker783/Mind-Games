import brain_games.engine.cli as cli
from brain_games.games.prime import game


def main():
    cli.welcome_user()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    if game():
        cli.game_ending()


if __name__ == "__main__":
    main()
