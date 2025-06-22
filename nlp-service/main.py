from fastapi import FastAPI
from models import TextInput
from analyzer import analyze_text

app = FastAPI()

@app.post("/analyze")
async def analyze(input_text: TextInput):
    result = analyze_text(input_text.text)
    return result

