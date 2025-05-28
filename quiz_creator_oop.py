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
            