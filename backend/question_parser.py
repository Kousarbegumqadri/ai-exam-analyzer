import re

def extract_questions(text):
    questions = re.split(r'\d+\.', text)  # split by 1. 2. 3.
    return [q.strip() for q in questions if len(q.strip()) > 20]