import os 
import time
from datetime import datetime

class Quiz:
    def __init__(self):
        self.dict_quiz = {}
        self.question_number = 1 
        self.choice_labels = ['A', 'B', 'C', 'D'] 

    def add_question(self):
        question_input = input("Enter Question: ")
        choices_dict = {}
        print ("Enter the 4 choices: ")
        for label in self.choice_labels:
            choice_text = input (f"Choice {label}: ")
            choices_dict[label] = choice_text
        answer_input = input("Enter Answer (The Letter): ").upper()

        self.dict_quiz[f"Question {self.question_number}"] = {
            "Question": question_input,
            "Choices": choices_dict,
            "Answer": answer_input
        }

        self.question_number += 1
        
    def edit_question(self):
        print("\nQuestions:")
        for question_id in self.dict_quiz:
            print(question_id)
        
        to_edit = input("Please enter the Question number to edit (number only): ")
        key = f"Question {to_edit}"
        if key in self.dict_quiz:
            print(f"\nEditing {key}")
            new_question = input("Enter new question: ")
            new_choices = {}
            print("Enter the new 4 choices: ")
            for label in self.choice_labels:
                new_choice = input(f"Choice {label}: ")
                new_choice[label] = new_choice
            new_answer = input("Enter new correct answer (The letter): ").upper()
            self.dict_quiz[key] = {
                "Question": new_question,
                "Choices": new_choices,
                "Answer": new_answer,

            }

        else: 
            print("Invalid question number.")

    def delete_question(self):
        print("\nQuestions:")
        for question_id in self.dict_quiz:
            print(question_id)

        to_delete = input("Please enter the Question number to delete (number only): ")
        key = f"Question [to_delete]"
        if key in self.dict_quiz:
            del self.dict_quiz[key]
            print(f"Successfully deleted {key}")
        else:
            print("Invalid question number.")

    def save_quiz(self):
        RED = '\033[91m'
        RESET = '\033[0m'
        quiz_file_name = input(f"\n{RED}!! Make sure file name is unique to avoid overwriting !!{RESET} \nPlease Enter File Name: ")
        print("\nQuiz Summary: ")
        for question_id, data in self.dict_quiz.items():
            print(f"\n[question_id]: {data['Question']}")
            for letter, choice in data['Choices'].items():
                print(f"    {letter}. {choice}")
            print(f"Answer: {data['Answer']}")

        folder_name = "Quizzes"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        file_name = os.path.join(folder_name, quiz_file_name)

        with open(file_name, "w") as file:
            file.write ("\n" + "~" * 40 + "\n")
            file.write (f"Created New Quiz at - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write ("\n" + "~" * 40 + "\n")

            for question_id, data in self.dict_quiz.items():
                file.write(f"\n{question_id}: {data['Question']}\n")
                for letter, choice in data['Choices'].items():
                    file.write(f"    {letter}. {choice}\n")
                file.write(f"Answer: {data['Answer']}\n\n")

        print("Saving quiz", end='', flush=True)
        for msg in [" .", " ..", " ..."]:
            time.sleep(0.5)
            print(msg, end='', flush=True)
        print(f"\nDone! File saved as '{quiz_file_name}.txt'")

    def run(self):
        while True:
            exit_prompt = input("Continue adding question? (yes/edit/delete/exit): ").lower()

            if exit_prompt == "edit":
                self.edit_question()
            elif exit_prompt == "delete":
                self.delete_question()
            elif exit_prompt == "yes":
                break
            elif exit_prompt == "exit":
                self.save_quiz()
                exit()
            else:
                print("Invalid input. Please enter yes/edit/delete/exit.")


if __name__ == "__main__":
    quiz = Quiz()
    quiz.run()