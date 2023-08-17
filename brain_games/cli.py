import prompt

name = ''


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")


def game_ending():
    print(f"Congratulations, {name}!")
