import argparse
import sys
from .input_handler import InputHandler
from .inverse_nlp_engine import InverseNLPEngine
from .report_generator import ReportGenerator

def main():
    """
    Función principal para la Interfaz de Línea de Comandos (CLI) del PNLIO-Framework.
    """
    parser = argparse.ArgumentParser(
        description="PNLIO-Framework CLI: Herramienta de Discernimiento para el output de IA.",
        epilog="Uso: python -m pnlio.cli \"Texto de la IA a analizar\""
    )
    parser.add_argument(
        "ia_output",
        type=str,
        help="El texto (output) del Agente de IA que se desea analizar."
    )
    parser.add_argument(
        "-a", "--author",
        type=str,
        default="Gonzalo de la Rivera Arellano",
        help="Nombre del autor del concepto de PNL Inversa Ontológica para la atribución."
    )
    
    args = parser.parse_args()

    try:
        # 1. Inicialización de Componentes
        input_handler = InputHandler()
        engine = InverseNLPEngine()
        report_generator = ReportGenerator(author_name=args.author)

        # 2. Procesamiento
        input_handler.load_text(args.ia_output)
        analysis_results = engine.analyze_text(input_handler.raw_text)

        # 3. Generación del Reporte
        report = report_generator.generate_report(analysis_results)

        # 4. Impresión del Reporte
        print("\n" + "="*70)
        print("INFORME DE DISCERNIMIENTO PNLIO (CLI)")
        print("="*70)
        print(report)
        print("="*70)

    except ValueError as e:
        print(f"Error de Entrada: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error Inesperado: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
