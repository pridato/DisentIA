from transformers import pipeline, XLMRobertaTokenizer
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def zero_shot_analysis(text: str, labels: list[str], model_name: str, hypothesis_template: str) -> dict:
    """
    Realiza un análisis de clasificación de texto utilizando un modelo de zero-shot learning.
    :param text: Texto a clasificar.
    :param labels: Lista de etiquetas candidatas para la clasificación.
    :param model_name: Nombre del modelo a utilizar para la clasificación.
    :param hypothesis_template: Plantilla de hipótesis para la clasificación.
    :return:
    """
    logging.info(f"Starting zero-shot analysis with model: {model_name}")
    tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)

    classifier = pipeline(
        "zero-shot-classification",
        model=model_name,
        tokenizer=tokenizer,
        hypothesis_template=hypothesis_template
    )

    result = classifier(text, candidate_labels=labels)
    return result