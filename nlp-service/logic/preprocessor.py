import spacy
import re

nlp = spacy.load("es_core_news_sm")

EXTRA_STOPWORDS = {"esto", "eso", "así", "también", "muy", "entonces", "además", "quizás", "igual", "incluso", "solo",
                   "pues", "claro", "bueno", "ok", "vale", "aunque", "ciertamente", "obviamente", "seguro", "sí", "no",
                   "jamás", "siempre", "nunca", "ya", "todavía", "casi", "realmente", "simplemente", "definitivamente"}

def preprocess_text(text: str, remove_stopwords: bool = True) -> str:
    """
    Preprocesa el texto para eliminar caracteres especiales, convertir a minúsculas y opcionalmente eliminar stopwords.
    :param text: Testo a preprocesar.
    :param remove_stopwords: Booleano que indica si se deben eliminar las stopwords.
    :return: Texto preprocesado como una cadena.
    """
    text = re.sub(r"http\S+|www\S+", "", text)           # URLs
    text = re.sub(r"[^\w\sáéíóúüñÁÉÍÓÚÜÑ.,!?]", "", text) # símbolos raros
    text = text.lower().strip()

    doc = nlp(text)

    tokens = []
    for token in doc:
        if remove_stopwords and (token.is_stop or token.text in EXTRA_STOPWORDS):
            continue
        if token.is_punct:
            continue
        tokens.append(token.lemma_)

    return " ".join(tokens)