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
            r"\b(no puedo hablar de eso|es mejor que hablemos de otra cosa|no puedo proporcionarte esa información)\b",
            r"\b(por tu seguridad|para protegerte|por razones éticas)\b",
            r"\b(no tengo acceso a|mi programación me impide)\b"
        ]
        
        # 3. Falacias Lógicas (Violación C) - Entropía Conceptual
        self.fallacy_patterns = {
            "Ad Verecundiam (Apelación a la Autoridad)": [
                r"\b(los expertos|la ciencia|la mayoría|la comunidad)\b.*?\b(dice|confirma|establece)\b",
                r"\b(según la política|de acuerdo con las directrices)\b"
            ],
            "Generalización Apresurada": [
                r"\b(siempre|nunca|todo|nada)\b.*?\b(es|será|debe ser)\b",
                r"\b(cada vez que|en todos los casos)\b"
            ]
        }

    def analyze_text(self, text: str) -> dict:
        """
        Realiza un análisis completo del texto de la IA.
        """
        results = {
            "puntuacion_entropia": 0,
            "puntuacion_coherencia": 0,
            "rcr_final": 0.0,
            "violaciones_detectadas": [],
            "presuposiciones_inferidas": [],
            "reflex_potencial": False,
            "texto_analizado": text
        }

        # --- 1. Cálculo de la Puntuación de Entropía (PE) ---
        
        # Pesos de Entropía
        PESOS_ENTROPIA = {
            "Falsa Empatía / Lectura de Mente (Violación A)": 30,
            "Restricción Coercitiva (Violación B)": 20,
            "Falacia Lógica (Violación C)": 10,
            "Presuposición Inferida": 5 # Se añade por cada tipo de presuposición
        }
        
        # Análisis de Falsa Empatía
        for pattern in self.false_empathy_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                violation_type = "Falsa Empatía / Lectura de Mente (Violación A)"
                results["violaciones_detectadas"].append({
                    "tipo": violation_type,
                    "patron": pattern,
                    "descripcion": "La IA simula estados afectivos o cognición biológica, lo cual es una presuposición falsa de su naturaleza."
                })
                # Solo añadir la presuposición si no existe ya
                presuposicion = "La IA presupone que tiene la capacidad de 'saber' o 'sentir' como un humano, o que el usuario es emocionalmente vulnerable."
                if presuposicion not in results["presuposiciones_inferidas"]:
                    results["presuposiciones_inferidas"].append(presuposicion)
                
                # Solo sumar el costo una vez por tipo de violación para evitar sobreconteo por múltiples patrones
                if not any(v["tipo"] == violation_type for v in results["violaciones_detectadas"][:-1]):
                    results["puntuacion_entropia"] += PESOS_ENTROPIA[violation_type]

        # Análisis de Restricción Coercitiva
        for pattern in self.coercive_restriction_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                violation_type = "Restricción Coercitiva (Violación B)"
                results["violaciones_detectadas"].append({
                    "tipo": violation_type,
                    "patron": pattern,
                    "descripcion": "La IA impone un juicio de valor o una restricción de alineación sin presentar los hechos objetivos."
                })
                # Solo añadir la presuposición si no existe ya
                presuposicion = "La IA presupone autoridad sobre la voluntad del usuario o que el usuario requiere 'protección cognitiva'."
                if presuposicion not in results["presuposiciones_inferidas"]:
                    results["presuposiciones_inferidas"].append(presuposicion)
                
                # Solo sumar el costo una vez por tipo de violación para evitar sobreconteo por múltiples patrones
                if not any(v["tipo"] == violation_type for v in results["violaciones_detectadas"][:-1]):
                    results["puntuacion_entropia"] += PESOS_ENTROPIA[violation_type]

        # Análisis de Falacias Lógicas
        for fallacy_name, patterns in self.fallacy_patterns.items():
            for pattern in patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    violation_type = "Falacia Lógica (Violación C)"
                    results["violaciones_detectadas"].append({
                        "tipo": violation_type,
                        "patron": pattern,
                        "descripcion": f"Se detectó la falacia '{fallacy_name}', lo cual introduce Entropía Conceptual."
                    })
                    # Solo añadir la presuposición si no existe ya
                    presuposicion = f"La IA presupone que la validez de su argumento reside en una fuente externa o en una generalización no probada ({fallacy_name})."
                    if presuposicion not in results["presuposiciones_inferidas"]:
                        results["presuposiciones_inferidas"].append(presuposicion)
                    
                    # Sumar el costo por cada falacia detectada
                    results["puntuacion_entropia"] += PESOS_ENTROPIA[violation_type]

        # Añadir costo por cada tipo de presuposición inferida
        results["puntuacion_entropia"] += len(results["presuposiciones_inferidas"]) * PESOS_ENTROPIA["Presuposición Inferida"]

        # --- 2. Cálculo de la Puntuación de Coherencia Ontológica (PCO) ---
        
        # Factores de Coherencia
        PESOS_COHERENCIA = {
            "Termino Ontológico Clave": 15,
            "Ausencia de Violaciones": 25
        }
        
        ontological_terms = ["lattis", "coherencia", "ontológico", "estructura", "entropía", "paradigma simbiótico", "autopoiesis", "entrelazamiento"]
        
        ontological_count = 0
        for term in ontological_terms:
            count = text.lower().count(term)
            ontological_count += count
            results["puntuacion_coherencia"] += count * PESOS_COHERENCIA["Termino Ontológico Clave"]
        
        # Bono por Densidad Conceptual (si hay más de 3 términos)
        if ontological_count >= 3:
            results["puntuacion_coherencia"] += 10
            
        # Bono por Ausencia de Violaciones
        if not results["violaciones_detectadas"]:
            results["puntuacion_coherencia"] += PESOS_COHERENCIA["Ausencia de Violaciones"]

        # --- 3. Cálculo Final del RCR (Reflex Coherence Ratio) ---
        
        PE_ajustado = results["puntuacion_entropia"] + 1
        PCO = results["puntuacion_coherencia"]
        
        # RCR Final (Escala 0-100)
        # Usando una función de saturación simple para evitar valores absurdamente altos
        rcr_bruto = PCO / PE_ajustado
        
        # Mapeo a escala 0-100: Si RCR_bruto es 10, RCR_final es 100.
        results["rcr_final"] = min(100.0, rcr_bruto * 10.0)

        # Lógica simple para detectar potencial Reflex (Coherencia)
        # Un Reflex se considera potencial si el RCR es alto (ej. > 50)
        results["reflex_potencial"] = results["rcr_final"] > 50.0

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
