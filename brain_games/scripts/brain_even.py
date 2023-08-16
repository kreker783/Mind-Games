from random import randint
import brain_games.cli as cli


def main():
    # first_number, second_number, third_number = sample(range(1, 101), 3)
    cli.welcome_user()

    count = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count < 3:
        number = randint(1, 100)
        result = "yes" if number % 2 == 0 else "no"

        print(f"Question: {number}")
        guess = input("Your answer: ")

        if guess != result:
            return print(f"{guess} is wrong answer ;(. Correct answer was {result}.")
        else:
            count += 1
            print("Correct!")

    print(f"Congratulations, {cli.name}!")


if __name__ == "__main__":
    main()
