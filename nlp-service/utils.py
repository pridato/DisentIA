def top_n_labels(result: dict, n=5) -> dict:
    """
    Obtiene las n etiquetas con mayor puntuación de un resultado de análisis de zero-shot.
    :param result: dict: Resultado del análisis de zero-shot, que contiene "labels" y "scores".
    :param n: int: Número de etiquetas a devolver.
    :return: dict: Un diccionario con las etiquetas y sus puntuaciones correspondientes.
    """
    pairs = list(zip(result["labels"], result["scores"]))
    top = sorted(pairs, key=lambda x: x[1], reverse=True)[:n]
    return {
        "labels": [label for label, _ in top],
        "scores": [score for _, score in top]
    }