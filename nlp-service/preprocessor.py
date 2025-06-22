import spacy
import re
from consts import EXTRA_STOPWORDS


nlp = spacy.load("es_core_news_sm")


def preprocess_text(text: str, remove_stopwords: bool = True) -> str:
    """
    Preprocesa el texto para eliminar caracteres especiales, convertir a minúsculas y opcionalmente eliminar stopwords.
    :param text: Testo a preprocesar.
    :param remove_stopwords: Booleano que indica si se deben eliminar las stopwords.
    :return: Texto preprocesado como una cadena.
    """

    # limpiamos el texto de urls y caracteres especiales
    text = re.sub(r"http\S+|www\S+", "", text)           # URLs
    text = re.sub(r"[^\w\sáéíóúüñÁÉÍÓÚÜÑ.,!?]", "", text) # símbolos raros
    text = text.lower().strip()

    # procesamos el texto con spaCy, lo dejamos preparado para aplicar lematización y stopwords
    doc = nlp(text)

    tokens = []
    for token in doc: # recorremos los tokens del documento
        if remove_stopwords and (token.is_stop or token.text in EXTRA_STOPWORDS):
            # eliminamos stopwords y extra stopwords (si corresponde)
            continue
        if token.is_punct:
            # si es un signo de puntuación, lo eliminamos
            continue
        tokens.append(token.lemma_)

    return " ".join(tokens)