import brain_games.engine.cli as cli
from brain_games.games.progression import game


def main():
    cli.welcome_user()

    print('What number is missing in the progression?')

    if game():
        cli.game_ending()


if __name__ == "__main__":
    main()
