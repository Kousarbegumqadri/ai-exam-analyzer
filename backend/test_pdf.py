from pdf_extractor import extract_text
from question_parser import extract_questions

text = extract_text("sample.pdf")

questions = extract_questions(text)

for i, q in enumerate(questions):
    print(f"{i+1}. {q}")