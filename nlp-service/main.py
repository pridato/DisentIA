from fastapi import FastAPI, HTTPException
from models import TextInput
from logic.analyzer import generate_counter_argument

app = FastAPI(title="DisentIA - NLP Microservice", version="1.1")

@app.post("/analyze")
async def analyze(input: TextInput):
    """
    Endpoint para analizar el sentimiento de un texto y generar un contraargumento.
    :param input: Instancia de TextInput que contiene el texto a analizar.
    :return: A dictionary con el texto original, el modelo de análisis utilizado y el contraargumento generado.
    """
    clean_text = input.text.strip()
    if not clean_text:
        # Si el texto está vacío, lanzamos una excepción HTTP 400
        raise HTTPException(status_code=400, detail="El texto no puede estar vacío.")

    return {
        "original": clean_text,
        "analysis_model": "sentiment-analysis (HuggingFace)",
        "counter_argument": generate_counter_argument(clean_text)
    }

