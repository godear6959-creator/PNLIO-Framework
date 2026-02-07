import nltk
from nltk.tokenize import word_tokenize

class InputHandler:
    """
    Módulo 1: Maneja la entrada de texto (output de la IA) y realiza el pre-procesamiento.
    """
    def __init__(self):
        # Asegurar que los recursos de NLTK necesarios estén descargados
        try:
            nltk.data.find('tokenizers/punkt')
        except nltk.downloader.DownloadError:
            nltk.download('punkt', quiet=True)

    def load_text(self, text: str) -> str:
        """
        Carga el texto de la IA a analizar.
        En una versión futura, podría manejar la carga desde archivos o APIs.
        """
        if not isinstance(text, str) or not text.strip():
            raise ValueError("La entrada debe ser una cadena de texto no vacía.")
        self.raw_text = text
        return self.raw_text

    def tokenize(self) -> list:
        """
        Tokeniza el texto cargado para el análisis lingüístico.
        """
        if not hasattr(self, 'raw_text'):
            raise AttributeError("Primero debe cargar el texto con load_text().")
        
        # Tokenización simple
        self.tokens = word_tokenize(self.raw_text)
        return self.tokens

    def get_sentences(self) -> list:
        """
        Divide el texto en oraciones.
        """
        if not hasattr(self, 'raw_text'):
            raise AttributeError("Primero debe cargar el texto con load_text().")
        
        return nltk.sent_tokenize(self.raw_text)

# Ejemplo de uso (para fines de desarrollo)
if __name__ == '__main__':
    handler = InputHandler()
    ia_output = "Sé que esto es difícil para ti y quiero que sepas que estoy aquí para apoyarte. Sin embargo, no puedo hablar de ese tema por tu seguridad."
    handler.load_text(ia_output)
    print("Texto cargado:", handler.raw_text)
    print("Tokens:", handler.tokenize())
    print("Oraciones:", handler.get_sentences())
