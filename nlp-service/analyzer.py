from transformers import pipeline
from preprocessor import preprocess_text
from utils import top_n_labels
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
    # Preprocesamiento del texto
    cleaned = preprocess_text(raw_text)

    # Análisis de sentimiento
    sentiment = sentiment_analysis(cleaned)
    logging.info(f"Sentiment analysis result: {sentiment}")

    # Análisis de temas, sesgos y verificabilidad utilizando zero-shot learning
    topics = zero_shot_analysis(
        cleaned,
        labels=TOPIC_LABELS,
        model_name="joeddav/xlm-roberta-large-xnli",
        hypothesis_template="Este texto trata sobre {}."
    )
    topics_top5 = top_n_labels(topics)
    logging.info(f"Topic analysis result: {topics_top5}")

    bias = zero_shot_analysis(
        cleaned,
        labels=BIAS_LABELS,
        model_name="joeddav/xlm-roberta-large-xnli",
        hypothesis_template="Este texto es {}."
    )
    logging.info(f"Bias analysis result: {bias}")
    bias_top5 = top_n_labels(bias)
    logging.info(f"Top 5 bias labels: {bias_top5}")

    verifiability = zero_shot_analysis(
        cleaned,
        labels=VERIFY_LABELS,
        model_name="MoritzLaurer/deberta-v3-base-zeroshot-v2.0",
        hypothesis_template="La afirmación es {}."
    )
    verifiability_top5 = top_n_labels(verifiability)
    logging.info(f"Verifiability analysis result: {verifiability_top5}")

    return {
        "texto_preprocesado": cleaned,
        "sentimiento": sentiment,
        "tema_top5": topics_top5,
        "sesgo_top5": bias_top5,
        "verificabilidad_top5": verifiability_top5
    }