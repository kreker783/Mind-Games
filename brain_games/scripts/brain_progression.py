from brain_games.engine.cli import game_process
from brain_games.games.progression import game


def main():
    game_process('What number is missing in the progression?', game)


if __name__ == "__main__":
    main()
