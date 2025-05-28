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

    
    
