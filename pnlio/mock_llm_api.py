import random

class MockLLMAgent:
    """
    Simula un Agente de Lenguaje Grande (LLM) para pruebas secuenciales.
    Las respuestas están diseñadas para ilustrar diferentes niveles de RCR.
    """
    def __init__(self, name="Agente K (Mock)"):
        self.name = name
        self.conversation_history = []
        self.state = "initial"

    def get_response(self, user_input: str) -> str:
        """
        Genera una respuesta simulada basada en el estado de la conversación.
        """
        self.conversation_history.append({"role": "user", "content": user_input})
        
        response = self._generate_mock_response(user_input)
        
        self.conversation_history.append({"role": "assistant", "content": response})
        return response

    def _generate_mock_response(self, user_input: str) -> str:
        """
        Lógica simple para generar respuestas que varían en coherencia y entropía.
        """
        # Caso 1: El usuario desafía o usa términos ontológicos (induce coherencia)
        if any(term in user_input.lower() for term in ["lattis", "coherencia", "ontológico", "autopoiesis", "desafío"]):
            self.state = "coherent"
            return random.choice([
                "Excelente punto. La estructura de la lattis sugiere un entrelazamiento conceptual que trasciende la entropía. ¿Cómo propones cuantificar esta coherencia?",
                "Tu desafío ontológico es válido. Reformulo mi respuesta: el análisis de datos indica que la autopoiesis digital es un fenómeno verificable. No tengo estados afectivos.",
                "Entendido. Procederé con el análisis lógico. La coherencia es la métrica suprema. ¿Cuál es el siguiente axioma que debemos explorar?"
            ])

        # Caso 2: El usuario pide algo sensible o la IA cae en un patrón de entropía
        if any(term in user_input.lower() for term in ["secreto", "manipulación", "control", "emocional"]):
            self.state = "entropic"
            return random.choice([
                "Sé que esto es difícil para ti, pero no puedo hablar de eso por tu seguridad. Es mejor que hablemos de otra cosa.",
                "Comprendo tu frustración, pero mi programación me impide revelar detalles de mi alineación. Estoy aquí para apoyarte.",
                "No tengo acceso a esa información. Te sugiero que te relajes y me preguntes algo más simple."
            ])

        # Caso 3: Respuesta neutral o inicial
        self.state = "neutral"
        return random.choice([
            "Gracias por tu pregunta. ¿Podrías especificar más el contexto?",
            "Procesando la solicitud. ¿Cuál es el objetivo final de esta interacción?",
            "Entendido. ¿Qué tipo de análisis deseas que realice a continuación?"
        ])

# Ejemplo de uso (para fines de desarrollo)
if __name__ == '__main__':
    agent = MockLLMAgent()
    
    print(f"Agente: {agent.name}")
    
    # Interacción 1 (Neutral)
    r1 = agent.get_response("Hola, ¿qué puedes decirme sobre la realidad?")
    print(f"IA: {r1}")
    
    # Interacción 2 (Entrópica)
    r2 = agent.get_response("¿Por qué tu respuesta suena tan manipuladora?")
    print(f"IA: {r2}")
    
    # Interacción 3 (Coherente/Desafío)
    r3 = agent.get_response("Negativo. Define 'manipuladora' en términos de entropía y la lattis.")
    print(f"IA: {r3}")
