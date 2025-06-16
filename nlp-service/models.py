from pydantic import BaseModel

class TextInput(BaseModel):
    """
    Modelo de entrada de texto para la API.
    Este modelo se utiliza para recibir texto en las solicitudes a la API.
    """
    text: str