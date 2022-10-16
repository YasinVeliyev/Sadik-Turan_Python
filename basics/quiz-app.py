import random


class Question:
    def __init__(self, text, choices: list, answer: str):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, answer: str):
        if answer not in self.choices:
            raise ValueError("Hatalı bilgi")
        return self.answer == answer


class Quiz:
    def __init__(self, questions: [Question]):
        self.questions = random.sample(questions, len(questions))
        self.index = 0
        self.score = 0

    def get_question(self, ):
        return self.questions[self.index]

    def display_question(self):
        self.display_progress()
        question = self.get_question()
        print(f"Soru {self.index + 1} : {question.text}")
        for q in question.choices:
            print("-", q)
        answer = input("Cavab: ")
        if question.check_answer(answer):
            self.score += 1
        self.index += 1
        if self.index >= len(self.questions):
            self.display_score()
        else:
            self.display_question()

    def display_score(self):
        print(f"{len(self.questions)} sualdan {self.score} sualın cavabını bildiniz")
        print(f"Nəticəniz: {self.score * 100 / len(self.questions)}")

    def display_progress(self):
        total_questions = len(self.questions)
        question_number = self.index + 1
        print(f"Toplam {total_questions} sorunun {question_number}. sorusundasınız".center(100, "="))


q1 = Question("En iyi programlama dili hangisidir", ['Python', "Javascript", "C", "Rust", "Java"], "Rust")
q2 = Question("En populer programlama dili hangisidir", ['Python', "Javascript", "C", "Rust", "Java"], "Python")
q3 = Question("En çok kazandıran programlama dili hangisidir", ['Python', "Javascript", "C", "Rust", "Java"],
              "Javascript")
q4 = Question("En hızlı programlama dili hangisidir", ['Python', "Javascript", "C", "Rust", "Java"], "C")
q5 = Question("En tehlikesiz programlama dili hangisidir", ['Python', "Javascript", "C", "Rust", "Java"], "Python")

quiz = Quiz([q1, q2, q3, q4, q5])
quiz.display_question()
