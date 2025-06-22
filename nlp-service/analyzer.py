from transformers import pipeline
from preprocessor import preprocess_text
from zero_shot import zero_shot_analysis
from consts import TOPIC_LABELS, BIAS_LABELS, VERIFY_LABELS
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def sentiment_analysis(text: str) -> str:
    """
    Realiza un análisis de sentimiento del texto utilizando un modelo preentrenado.
    :param text: Texto a analizar.
    :return: Etiqueta de sentimiento del texto.
    """
    classifier = pipeline("sentiment-analysis", model="pysentimiento/robertuito-sentiment-analysis")
    return classifier(text)[0]["label"]

def analyze_text(raw_text: str) -> dict:
    """
    Analiza el texto dado realizando preprocesamiento, análisis de sentimiento, temas, sesgos y verificabilidad.
    :param raw_text: Texto en bruto a analizar.
    :return: dict: Un diccionario con los resultados del análisis.
    """
    cleaned = preprocess_text(raw_text)

    sentiment = sentiment_analysis(cleaned)
    logging.info(f"Sentiment analysis result: {sentiment}")

    topics = zero_shot_analysis(
        cleaned,
        labels=TOPIC_LABELS,
        model_name="joeddav/xlm-roberta-large-xnli",
        hypothesis_template="Este texto trata sobre {}."
    )
    logging.info(f"Topic analysis result: {topics}")

    bias = zero_shot_analysis(
        cleaned,
        labels=BIAS_LABELS,
        model_name="joeddav/xlm-roberta-large-xnli",
        hypothesis_template="Este texto es {}."
    )
    logging.info(f"Bias analysis result: {bias}")

    verifiability = zero_shot_analysis(
        cleaned,
        labels=VERIFY_LABELS,
        model_name="microsoft/deberta-v3-base-mnli",
        hypothesis_template="La afirmación es {}."
    )
    logging.info(f"Verifiability analysis result: {verifiability}")

    return {
        "texto_preprocesado": cleaned,
        "sentimiento": sentiment,
        "tema": topics,
        "sesgo": bias,
        "verificabilidad": verifiability
    }