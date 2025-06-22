from transformers import pipeline
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def zero_shot_analysis(text: str, labels: list[str], model_name: str, hypothesis_template: str) -> dict:
    """
    Realiza un análisis de clasificación de texto utilizando un modelo de zero-shot learning.
    """
    logging.info(f"Starting zero-shot analysis with model: {model_name}")

    classifier = pipeline(
        "zero-shot-classification",
        model=model_name,
        hypothesis_template=hypothesis_template
    )

    result = classifier(text, candidate_labels=labels)
    return result