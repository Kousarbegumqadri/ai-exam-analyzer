from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid

from analyzer import analyze

app = FastAPI()

# -----------------------------
# CORS (IMPORTANT for React)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Upload folder
# -----------------------------
UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# -----------------------------
# Root route (optional check)
# -----------------------------
@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}

# -----------------------------
# MAIN API: Upload + Analyze PDF
# -----------------------------
@app.post("/analyze/")
async def analyze_paper(file: UploadFile = File(...)):

    # check file type
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files allowed"}

    # generate unique filename
    filename = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # save file
    content = await file.read()
    with open(file_path, "wb") as buffer:
        buffer.write(content)

    # run your analyzer
    result = analyze(file_path)

    # return response to frontend
    return {
        "result": result,
        "file_path": file_path
    }