# Primera lógica basica para analizar el sentimiento de un texto y generar un contraargumento.
from transformers import pipeline


classifier = pipeline("sentiment-analysis")

def generate_counter_argument(text: str) -> str:
    """
    Genera un contraargumento basado en el análisis de sentimiento del texto proporcionado.
    :param text: Texto a analizar para generar un contraargumento.
    :return: Un contraargumento basado en el análisis de sentimiento del texto.
    """
    result = classifier(text)[0]
    label = result["label"]

    if label == "POSITIVE":
        return "Aunque suene optimista, también hay riesgos en la implementación masiva de IA."
    elif label == "NEGATIVE":
        return "A pesar de las preocupaciones, la IA también tiene potencial para mejorar nuestras vidas."
    else:
        return "Es importante analizar la evidencia antes de asumir conclusiones sobre la IA."