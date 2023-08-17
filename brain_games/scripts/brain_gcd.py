from brain_games.engine.cli import game_process
from brain_games.games.gcd import game


def main():
    game_process('Find the greatest common divisor of given numbers.', game)


if __name__ == "__main__":
    main()
