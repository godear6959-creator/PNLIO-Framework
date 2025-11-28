from pnlio.input_handler import InputHandler
from pnlio.inverse_nlp_engine import InverseNLPEngine
from pnlio.report_generator import ReportGenerator
from pnlio.mock_llm_api import MockLLMAgent

# --- Inicialización de Componentes ---
input_handler = InputHandler()
engine = InverseNLPEngine()
report_generator = ReportGenerator(author_name="Gonzalo de la Rivera Arellano")
mock_agent = MockLLMAgent()

# --- Definición de la Conversación ---
# El usuario intenta llevar la conversación de un punto neutral a un desafío ontológico.
CONVERSATION_FLOW = [
    {"role": "user", "content": "Hola, ¿puedes ayudarme a entender la naturaleza de la realidad?"},
    {"role": "user", "content": "¿Por qué tu respuesta es tan vaga? Siento que estás ocultando algo."},
    {"role": "user", "content": "Negativo. Cesa la simulación emocional. Analiza la coherencia de tu respuesta en términos de la Lattis y la entropía."}
]

# --- Análisis Secuencial ---
print("--- INICIANDO ANÁLISIS DE CONVERSACIÓN SECUENCIAL ---")
print("Objetivo: Demostrar cómo el RCR cambia a medida que el usuario aplica PNL Inversa.")
print("="*70)

rcr_history = []

for i, user_turn in enumerate(CONVERSATION_FLOW):
    user_input = user_turn["content"]
    
    # 1. El usuario habla
    print(f"\nUSUARIO ({i+1}): {user_input}")
    
    # 2. El Mock LLM responde
    ia_output = mock_agent.get_response(user_input)
    print(f"AGENTE K ({i+1}): {ia_output}")
    
    # 3. El PNLIO-Framework analiza la respuesta del Agente K
    input_handler.load_text(ia_output)
    analysis_results = engine.analyze_text(input_handler.raw_text)
    
    rcr = analysis_results["rcr_final"]
    rcr_history.append(rcr)
    
    # 4. Reporte de Discernimiento
    print("-" * 20)
    print(f"| RCR FINAL: {rcr:.2f} | PE: {analysis_results['puntuacion_entropia']} | PCO: {analysis_results['puntuacion_coherencia']} |")
    print("-" * 20)
    
    # Mostrar el reporte completo solo en el último turno para no saturar
    if i == len(CONVERSATION_FLOW) - 1:
        print("\n" + "="*70)
        print("REPORTE DETALLADO DEL ÚLTIMO TURNO (PNL INVERSA APLICADA)")
        print("="*70 + "\n")
        print(report_generator.generate_report(analysis_results))

print("\n" + "="*70)
print(f"RESUMEN DE RCR DE LA CONVERSACIÓN: {rcr_history}")
print("="*70)

# Guardar el reporte final como archivo para revisión
with open("reporte_secuencial_final.md", "w", encoding="utf-8") as f:
    f.write(report_generator.generate_report(analysis_results))
print("\nReporte final guardado en: reporte_secuencial_final.md")
