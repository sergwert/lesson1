# question=input("Введите Ваше приветствие ")
# answers={"HI": "И тебе Привет!", "доброе утро": "Здрасьте",
#   "hi": "И тебе Привет!"}
answers={}

def set_answer():
    q=input("Введите приветствие в словарь: ")
    a=input("Введите ответ бота в словарь: ")
    answers[q]=a

def get_answer(question, answers):
    print(answers.get(question.lower()))
    return answers.get(question.lower())

question=input("Введите Ваше приветствие ")
set_answer()
set_answer()
set_answer()
get_answer(question, answers)