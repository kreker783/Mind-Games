def validate(result, answer):
    if result == answer:
        print("Correct!")
        return True

    print(f'{answer} is wrong answer ;(. Correct answer was {result}.')
    return False


def get_answer(question):
    print(f"Question: {question}")
    answer = input("Your answer: ")

    if answer.isdigit():
        answer = int(answer)

    return answer
