import tkinter as tk
from tkinter import filedialog
import json
import random
import os
import time


class QuizPlayer:
    def __init__(self):
        self.quiz_information = {}
        self.user_score = 0
        self.folder_name = "imported_quiz"
        os.makedirs(self.folder_name, exists_ok=True)

    def list_quizzes(self):
        return [f for f in os.listdir(self.folder_name) if f.endswith(".json")]
    
    def import_new_quiz(self):
        print("Importing New Quiz", end='', flush=True)
        for msg in [" .", " ..", " ..."]:
            time.sleep(0.5)
            print(msg, end='', flush=True)

        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        quiz_file = filedialog.askopenfilename()
        root.destroy()

        if not quiz_file:
            print("No File Selected.")
            exit()

        current_question = None
        with open(quiz_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if "~" in line or "Created New Quiz at" in line or not line:
                    continue
                if line.startswith("Question"):
                    current_question = line.split(":")[0].strip()
                    self.quiz_information[current_question] = {
                        "Question": line.split(":", 1)[1].strip(),
                        "Choices": {},
                        "Answer": ""
                    }
                elif current_question and line[0] in ["A", "B", "C", "D"] and "." in line:
                    choice_label = line[0]
                    choice_text = line.split(".", 1)[1].strip()
                    self.quiz_information[current_question]["Choices"][choice_label] = choice_text
                elif current_question and "Answer" in line:
                    answer_part = line.split("Answer")[1].replace(":", "").strip()
                    self.quiz_information[current_question]["Answer"] = answer_part

        base_name = os.path.splitext(os.path.basename(quiz_file))[0]
        json_file_name = f"{base_name}.json"
        json_file_path = os.path.join(self.folder_name, json_file_name)

        if os.path.exists(json_file_path):
            base, ext = os.path.splitext(json_file_path)
            counter = 1
            while os.path.exists(f"{base}_{counter}{ext}"):
                counter += 1
            json_file_path = f"{base}_{counter}{ext}"

        with open(json_file_path, "w") as json_file:
            json.dump(self.quiz_information, json_file, indent=4)

        print(f"\nQuiz successfully saved as {os.path.basename(json_file_path)}")
    
    def load_existing_quiz(self, file_name):
        with open(os.path.join(self.folder_name, file_name), 'r') as json_file:
            self.quiz_information = json.load(json_file)
        print(f"\nLoaded Quiz Successfully: {file_name}")

    def take_quiz(self):
        print("\nLoading quiz...")
        questions = list(self.quiz_information.keys())
        random.shuffle(questions)

    def run(self):
        quizzes = self.list_quizzes()
        
        print("\nSelect an Option:")
        print("1. Import a new quiz")
        for idx, file in enumerate(quizzes, start=2):
            print(f"{idx}. {file}")
        print(f"{len(quizzes)+2}. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            self.import_new_quiz()
        elif choice.isdigit() and 2 <= int(choice) < len(quizzes) + 2:
            self.load_existing_quiz(quizzes[int(choice) - 2])
        else:
            print("Exiting", end='', flush=True)
            for msg in [" .", " ..", " ..."]:
                time.sleep(0.5)
                print(msg, end='', flush=True)
            exit()

        self.take_quiz()

if __name__ == "__main__":
    player = QuizPlayer()
    player.run()