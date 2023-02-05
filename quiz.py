quiz = {
    "question1": {
        "question": "What is the capital of India? ",
        "answer": "Delhi"
    },
    "question2": {
        "question": "What is the capital of USA? ",
        "answer": "Washington"
    },
    "question3": {
        "question": "What is the capital of United Kingdom? ",
        "answer": "London"
    },
    "question4": {
        "question": "What is the capital of France? ",
        "answer": "Paris"
    },
    "question5": {
        "question": "What is the capital of Germani? ",
        "answer": "Berlin"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")

    if answer.lower() == value["answer"].lower():
        print("Correct")
        score += 1              #similar to -> score = score + 1
        print(f"Your Score is: {score}")
        print("")
        print("")
    else:
        print("Wrong")
        print(f"The Answer is: {value['answer']}")
        print(f"Your Score is: {score}")
        print("")
        print("")

print(f"You got {score} out of 5 correctly!")
print(f"Your percentage is {int(score/5 * 100)}%")
