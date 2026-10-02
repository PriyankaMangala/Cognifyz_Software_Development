def show_welcome():
    print("="*40)
    print("         Python Quiz Game")
    print("="*40)
    print("Test your python knowledge!")
def choose_difficulty():
    print("choose your difficulty:")
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")

    while True:
        choice = input("\nEnter you choice(1-3):")
        if choice == "1":
            return "Easy"
        elif choice == "2":
            return "Medium"
        elif choice == "3":
            return "Hard"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
questions = {
    "Easy": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. def", "C. define", "D. fun"],
            "answer": "B"
        },
        {
            "question": "Which data type is used to store True or False?",
            "options": ["A. int", "B. str", "C. bool", "D. float"],
            "answer": "C"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["A. //", "B. /*", "C. #", "D. --"],
            "answer": "C"
        }
    ],

    "Medium": [
        {
            "question": "Which data structure stores key-value pairs?",
            "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
            "answer": "C"
        },
        {
            "question": "Which keyword is used to handle exceptions?",
            "options": ["A. error", "B. try", "C. catch", "D. handle"],
            "answer": "B"
        },
        {
            "question": "What does len() return?",
            "options": ["A. Data type", "B. Length of an object", "C. Memory size", "D. Index"],
            "answer": "B"
        }
    ],

    "Hard": [
        {
            "question": "Which concept allows a class to inherit properties from another class?",
            "options": ["A. Encapsulation", "B. Inheritance", "C. Abstraction", "D. Iteration"],
            "answer": "B"
        },
        {
            "question": "Which method is called automatically when an object is created?",
            "options": ["A. __start__", "B. __create__", "C. __init__", "D. __newobject__"],
            "answer": "C"
        },
        {
            "question": "What is the purpose of a Python decorator?",
            "options": [
                "A. Modify or extend a function's behavior",
                "B. Delete a function",
                "C. Create a database",
                "D. Compile Python code"
            ],
            "answer": "A"
        }
    ]
}
def play_quiz(selected_questions):
    score = 0
    for number, question in enumerate(selected_questions, start =1):
        print("\n" + "-" * 40)
        print(f"Question {number}")
        print(question["question"])
        for option in question["options"]:
            print(option)
        while True:
            user_answer = input("\nYour answer (A/B/C/D):").strip().upper()
            if user_answer in ["A", "B", "C","D"]:
                break
            else:
                print("Invalid answer. Please enter A,B, C, or D.")
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}.")
    return score


show_welcome()
difficulty = choose_difficulty()
print(f"\nYou selected: {difficulty}")
print("Let's begin!")
print("First question")
selected_questions = questions[difficulty]
score = play_quiz(selected_questions)
print("\n"+"="*40)
print("             RESULTS")
print("="*40)
print(f"Your score: {score}/{len(selected_questions)}")



