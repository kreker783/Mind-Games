from brain_games.engine.cli import game_process
from brain_games.games.even import game


def main():
    game_process('Answer "yes" if the number is even, otherwise answer "no".', game)


if __name__ == "__main__":
    main()
