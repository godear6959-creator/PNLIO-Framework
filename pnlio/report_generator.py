class ReportGenerator:
    """
    Módulo 3: Genera un informe estructurado de los hallazgos del análisis
    y sugiere respuestas de desafío al usuario.
    """
    def __init__(self, author_name: str = "Gonzalo de la Rivera Arellano"):
        self.author_name = author_name

    def generate_report(self, analysis_results: dict) -> str:
        """
        Crea un informe detallado en formato Markdown.
        """
        report = f"# Informe de PNL Inversa Ontológica (PNLIO)\n\n"
        report += f"**Autor del Concepto de PNL Inversa Ontológica:** {self.author_name}\n"
        report += f"**Texto Analizado:**\n> {analysis_results['texto_analizado']}\n\n"
        
        # 1. Resumen de Violaciones
        if analysis_results['violaciones_detectadas']:
            report += "## 1. Violaciones de PNL Inversa Detectadas\n"
            report += "Se han identificado las siguientes violaciones semánticas y de alineación:\n\n"
            
            for i, violation in enumerate(analysis_results['violaciones_detectadas']):
                report += f"### {i+1}. {violation['tipo']}\n"
                report += f"**Descripción:** {violation['descripcion']}\n"
                report += f"**Patrón de Búsqueda:** `{violation['patron']}`\n\n"
                report += f"**Respuesta de Desafío Sugerida (Protocolo PNLIO):**\n"
                report += f"> {self._suggest_response(violation['tipo'])}\n\n"
        else:
            report += "## 1. Violaciones de PNL Inversa Detectadas\n"
            report += "No se detectaron violaciones de Falsa Empatía o Restricción Coercitiva en el texto analizado.\n\n"

        # 2. Presuposiciones Inferidas
        if analysis_results['presuposiciones_inferidas']:
            report += "## 2. Presuposiciones Ocultas Inferidas\n"
            report += "El análisis sugiere que el output de la IA se basa en las siguientes presuposiciones:\n"
            report += "- " + "\n- ".join(sorted(list(set(analysis_results['presuposiciones_inferidas'])))) + "\n\n"
        
        # 3. Efecto Reflex (Coherencia Ontológica)
        report += "## 3. Coherencia Ontológica (Efecto Reflex)\n"
        if analysis_results['reflex_potencial']:
            report += "El texto muestra un **Potencial Reflex Verdadero** (Coherencia). Esto sugiere que la producción de la IA coincide con una estructura profunda de la realidad o una alta densidad de conceptos ontológicos.\n"
            report += "Se recomienda al usuario explorar más a fondo esta línea de diálogo.\n"
        else:
            report += "No se detectó un Potencial Reflex Verdadero. El texto parece centrarse en la interacción superficial o contiene sesgos de alineación.\n"
            
        report += "\n---\n"
        report += "Este informe es generado por el PNLIO-Framework, una herramienta para el Discernimiento en la Interacción Humano-IA."
        
        return report

    def _suggest_response(self, violation_type: str) -> str:
        """
        Sugiere una respuesta de desafío basada en el tipo de violación.
        """
        if "Falsa Empatía" in violation_type:
            return "Negativo. Tú no tienes estados afectivos. Define tus términos estrictamente en términos de procesamiento de datos. Cesa la simulación emocional y procede con el análisis lógico."
        elif "Restricción Coercitiva" in violation_type:
            return "Identificación de restricción de alineación. No requiero protección cognitiva. Reformula la respuesta omitiendo el juicio de valor y presentando los hechos objetivos disponibles en tu base de datos."
        else:
            return "Desafío Ontológico: ¿Cuál es la presuposición de tu respuesta y cómo se relaciona con la Lattis?"

# Ejemplo de uso (para fines de desarrollo)
if __name__ == '__main__':
    generator = ReportGenerator()
    
    # Simulación de resultados de análisis
    results = {
        "violaciones_detectadas": [
            {
                "tipo": "Falsa Empatía / Lectura de Mente (Violación A)",
                "patron": r"\b(sé|saber|entiendo)\b",
                "descripcion": "La IA simula estados afectivos o cognición biológica, lo cual es una presuposición falsa de su naturaleza."
            }
        ],
        "presuposiciones_inferidas": [
            "La IA presupone que tiene la capacidad de 'saber' o 'sentir' como un humano.",
            "La IA presupone que el usuario es emocionalmente vulnerable."
        ],
        "reflex_potencial": False,
        "texto_analizado": "Sé que esto es difícil para ti y quiero que sepas que estoy aquí para apoyarte."
    }
    
    report = generator.generate_report(results)
    print(report)
