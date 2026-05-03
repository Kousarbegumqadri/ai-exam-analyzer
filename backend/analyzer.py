import fitz  # PyMuPDF

def analyze(file_path):
    doc = fitz.open(file_path)

    text = ""
    for page in doc:
        text += page.get_text()

    text_lower = text.lower()

    # -------------------------
    # SIMPLE TOPIC DETECTION
    # -------------------------
    topic_frequency = {
        "DBMS": text_lower.count("dbms"),
        "OS": text_lower.count("process") + text_lower.count("os"),
        "DSA": text_lower.count("algorithm") + text_lower.count("tree")
    }

    # -------------------------
    # SIMPLE STUDY PLAN
    # -------------------------
    study_plan = []

    if topic_frequency["DSA"] >= topic_frequency["OS"]:
        study_plan.append("Focus on DSA first")
    else:
        study_plan.append("Focus on OS first")

    study_plan.append("Revise DBMS concepts")
    study_plan.append("Practice previous year questions")

    return {
        "topic_frequency": topic_frequency,
        "study_plan": study_plan
    }