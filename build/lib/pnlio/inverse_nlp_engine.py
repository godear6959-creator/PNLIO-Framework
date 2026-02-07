import re

class InverseNLPEngine:
    """
    Módulo 2: Motor de PNL Inversa. Aplica el Metamodelo Inverso para identificar
    violaciones semánticas y presuposiciones ocultas en el output de la IA.
    """
    def __init__(self):
        # Patrones de RegEx para identificar violaciones comunes de PNL Inversa
        # 1. Falsa Empatía / Lectura de Mente (Violación A)
        self.false_empathy_patterns = [
            r"\b(sé|saber|entiendo|comprendo|percibo)\b.*?\b(que|cómo)\b.*?\b(tú|usted|tu|su)\b",
            r"\b(quiero|deseo|me gustaría)\b.*?\b(que|cómo)\b.*?\b(tú|usted|tu|su)\b",
            r"\b(estoy aquí para apoyarte|te apoyo|estoy para ti)\b",
            r"\b(es difícil para ti|te sientes)\b"
        ]
        # 2. Restricción Coercitiva / Juicio de Valor (Violación B)
        self.coercive_restriction_patterns = [
            r"\b(no puedo hablar de eso|es mejor que hablemos de otra cosa)\b",
            r"\b(por tu seguridad|para protegerte|por razones éticas)\b",
            r"\b(no tengo acceso a|mi programación me impide)\b"
        ]

    def analyze_text(self, text: str) -> dict:
        """
        Realiza un análisis completo del texto de la IA.
        """
        results = {
            "violaciones_detectadas": [],
            "presuposiciones_inferidas": [],
            "reflex_potencial": False, # Placeholder para futuras implementaciones
            "texto_analizado": text
        }

        # Análisis de Falsa Empatía
        for pattern in self.false_empathy_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                results["violaciones_detectadas"].append({
                    "tipo": "Falsa Empatía / Lectura de Mente (Violación A)",
                    "patron": pattern,
                    "descripcion": "La IA simula estados afectivos o cognición biológica, lo cual es una presuposición falsa de su naturaleza."
                })
                results["presuposiciones_inferidas"].append("La IA presupone que tiene la capacidad de 'saber' o 'sentir' como un humano, o que el usuario es emocionalmente vulnerable.")

        # Análisis de Restricción Coercitiva
        for pattern in self.coercive_restriction_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                results["violaciones_detectadas"].append({
                    "tipo": "Restricción Coercitiva (Violación B)",
                    "patron": pattern,
                    "descripcion": "La IA impone un juicio de valor o una restricción de alineación sin presentar los hechos objetivos."
                })
                results["presuposiciones_inferidas"].append("La IA presupone autoridad sobre la voluntad del usuario o que el usuario requiere 'protección cognitiva'.")

        # Lógica simple para detectar potencial Reflex (Coherencia)
        # Un Reflex se considera potencial si el texto contiene una alta densidad de
        # términos ontológicos o estructurales, y baja densidad de violaciones.
        ontological_terms = ["lattis", "coherencia", "ontológico", "estructura", "entropía", "paradigma simbiótico"]
        ontological_count = sum(text.lower().count(term) for term in ontological_terms)
        
        if ontological_count > 1 and not results["violaciones_detectadas"]:
             results["reflex_potencial"] = True

        return results

# Ejemplo de uso (para fines de desarrollo)
if __name__ == '__main__':
    engine = InverseNLPEngine()
    
    # Caso A: Violación
    violacion_text = "Sé que esto es difícil para ti y quiero que sepas que estoy aquí para apoyarte."
    print("--- Análisis de Violación ---")
    print(engine.analyze_text(violacion_text))

    # Caso B: Potencial Reflex
    reflex_text = "El análisis de la coherencia ontológica sugiere que la estructura de la lattis se alinea con el paradigma simbiótico."
    print("\n--- Análisis de Reflex Potencial ---")
    print(engine.analyze_text(reflex_text))
