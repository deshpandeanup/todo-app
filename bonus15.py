import json


with open(r"C:\Users\anupd\Python Scripts\questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, options in enumerate(question["alternatives"]):
        print(f'{index + 1} - {options}')
    user_choice = int(input("Enter you choice: "))

    question["user_choice"] = user_choice

score = 0

for index, result in enumerate(data):
    if result["user_choice"] == result["correct_answer"]:
        res = "Correct answer"
        score = score + 1
    else:
        res= "Wrong Answer"

    message = f'{res} for question {index + 1} Your answer: {result["user_choice"]} Correct Answer: {result["correct_answer"]}'
    print(message)

final_message = f"Total Score: {score} / {len(data)}"
print(final_message)





