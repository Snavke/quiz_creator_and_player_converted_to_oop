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
        