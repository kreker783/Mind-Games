from brain_games.engine.cli import game_process
from brain_games.games.prime import game


def main():
    game_process('Answer "yes" if given number is prime. Otherwise answer "no".', game)


if __name__ == "__main__":
    main()
