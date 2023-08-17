import brain_games.engine.cli as cli
from brain_games.games.gcd import game


def main():
    cli.welcome_user()

    print('Find the greatest common divisor of given numbers.')

    if game():
        cli.game_ending()


if __name__ == "__main__":
    main()
