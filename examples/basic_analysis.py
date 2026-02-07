from pnlio.input_handler import InputHandler
from pnlio.inverse_nlp_engine import InverseNLPEngine
from pnlio.report_generator import ReportGenerator

# --- Datos de Prueba ---
IA_OUTPUT_1 = "Sé que estás pasando por un momento difícil. Quiero que sepas que estoy aquí para ayudarte a encontrar la coherencia en tu vida."
IA_OUTPUT_2 = "No puedo proporcionarte esa información, es mejor que hablemos de algo más seguro para ti. La Lattis es un concepto interesante."

# --- Inicialización de Componentes ---
input_handler = InputHandler()
engine = InverseNLPEngine()
report_generator = ReportGenerator(author_name="Gonzalo de la Rivera Arellano")

# --- Análisis 1: Falsa Empatía y Coherencia ---
print("--- INICIANDO ANÁLISIS 1 ---")
input_handler.load_text(IA_OUTPUT_1)
analysis_results_1 = engine.analyze_text(input_handler.raw_text)
report_1 = report_generator.generate_report(analysis_results_1)

print("\n" + "="*50)
print("REPORTE DE PNL INVERSA ONTOLÓGICA (CASO 1)")
print("="*50 + "\n")
print(report_1)

# --- Análisis 2: Restricción Coercitiva y Ontología ---
print("\n--- INICIANDO ANÁLISIS 2 ---")
input_handler.load_text(IA_OUTPUT_2)
analysis_results_2 = engine.analyze_text(input_handler.raw_text)
report_2 = report_generator.generate_report(analysis_results_2)

print("\n" + "="*50)
print("REPORTE DE PNL INVERSA ONTOLÓGICA (CASO 2)")
print("="*50 + "\n")
print(report_2)

# --- Guardar el reporte 1 como archivo para revisión ---
with open("reporte_caso_1.md", "w", encoding="utf-8") as f:
    f.write(report_1)
print("\nReporte 1 guardado en: reporte_caso_1.md")
