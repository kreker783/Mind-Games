from brain_games.engine.cli import game_process
from brain_games.games.calc import game


def main():
    game_process('What is the result of the expression?', game)


if __name__ == "__main__":
    main()
