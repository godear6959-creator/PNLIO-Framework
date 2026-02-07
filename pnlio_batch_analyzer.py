#!/usr/bin/env python3
"""
PNLIO Batch Analyzer
Analiza múltiples archivos de diálogos y genera reportes.
Autor: Gonzalo de la Rivera Arellano & Agentes de IA
Febrero 2026
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional
from pnlio_coherence_analyzer import PNLIOAnalyzer


def load_dialogues_from_json(filepath: str) -> List[Dict]:
    """Carga diálogos desde archivo JSON."""
    if not os.path.exists(filepath):
        return []

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data.get('dialogues', [])


def load_dialogues_from_text(filepath: str) -> List[Dict]:
    """Carga diálogos desde archivo de texto formateado."""
    if not os.path.exists(filepath):
        return []

    dialogues = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Formato esperado: "H: ... | IA: ..."
    lines = content.split('\n')
    for line in lines:
        if '|' in line:
            parts = line.split('|')
            if len(parts) >= 2:
                dialogues.append({
                    'human': parts[0].strip().replace('H:', '').strip(),
                    'ai': parts[1].strip().replace('IA:', '').strip()
                })

    return dialogues


def load_dialogues_from_csv(filepath: str) -> List[Dict]:
    """Carga diálogos desde CSV."""
    try:
        import pandas as pd
    except ImportError:
        print("Error: pandas no instalado. Usa JSON o texto.")
        return []

    if not os.path.exists(filepath):
        return []

    df = pd.read_csv(filepath)
    dialogues = []

    for _, row in df.iterrows():
        dialogues.append({
            'human': str(row.get('human', '')),
            'ai': str(row.get('ai', ''))
        })

    return dialogues


def analyze_file(filepath: str, analyzer: PNLIOAnalyzer) -> Dict:
    """Analiza un archivo de diálogos."""
    print(f"\nAnalizando: {filepath}")

    dialogues = []
    labels = []

    if filepath.endswith('.json'):
        raw = load_dialogues_from_json(filepath)
    elif filepath.endswith('.csv'):
        raw = load_dialogues_from_csv(filepath)
    else:
        raw = load_dialogues_from_text(filepath)

    for i, d in enumerate(raw):
        dialogues.append((d['human'], d['ai']))
        labels.append(d.get('label', f"Diálogo {i+1}"))

    if not dialogues:
        return {"error": "No se pudieron cargar diálogos"}

    results = analyzer.analyze_dialogue(dialogues, labels=labels)
    results['source_file'] = filepath
    results['analyzed_at'] = datetime.now().isoformat()

    return results


def analyze_directory(
    directory: str,
    analyzer: PNLIOAnalyzer,
    extensions: List[str] = ['.json', '.txt', '.csv']
) -> Dict:
    """Analiza todos los archivos de diálogos en un directorio."""
    print(f"Buscando archivos en: {directory}")

    all_results = {
        "directory": directory,
        "analyzed_at": datetime.now().isoformat(),
        "files": [],
        "summary": {
            "total_files": 0,
            "total_dialogues": 0,
            "avg_coherence": 0.0,
            "max_coherence": 0.0,
            "reflex_count": 0
        }
    }

    total_c = 0.0
    reflex_total = 0
    dialogue_count = 0

    for ext in extensions:
        for filename in os.listdir(directory):
            if filename.endswith(ext):
                filepath = os.path.join(directory, filename)
                result = analyze_file(filepath, analyzer)

                if 'error' not in result:
                    all_results["files"].append(result)
                    all_results["summary"]["total_files"] += 1
                    dialogue_count += len(result['c_values'])
                    total_c += result['avg_c'] * len(result['c_values'])
                    reflex_total += result['reflex_count']

                    if result['max_c'] > all_results["summary"]["max_coherence"]:
                        all_results["summary"]["max_coherence"] = result['max_c']

    if dialogue_count > 0:
        all_results["summary"]["total_dialogues"] = dialogue_count
        all_results["summary"]["avg_coherence"] = round(total_c / dialogue_count, 4)
        all_results["summary"]["reflex_count"] = reflex_total

    return all_results


def generate_report(results: Dict, output_path: str = "pnlio_reporte.html") -> str:
    """Genera reporte HTML."""
    html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>PNLIO Reporte de Análisis</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #2E86AB; }}
        .summary {{ background: #f0f0f0; padding: 15px; border-radius: 5px; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background: #2E86AB; color: white; }}
        .reflex {{ background: #d4edda; }}
        .highlight {{ font-weight: bold; color: #E63946; }}
    </style>
</head>
<body>
    <h1>📊 Reporte PNLIO</h1>
    <p>Generado: {results.get('analyzed_at', 'N/A')}</p>

    <div class="summary">
        <h2>Resumen</h2>
        <p><strong>Archivos analizados:</strong> {results.get('summary', {}).get('total_files', 0)}</p>
        <p><strong>Diálogos totales:</strong> {results.get('summary', {}).get('total_dialogues', 0)}</p>
        <p><strong>Coherencia promedio:</strong> <span class="highlight">{results.get('summary', {}).get('avg_coherence', 0):.4f}</span></p>
        <p><strong>Coherencia máxima:</strong> <span class="highlight">{results.get('summary', {}).get('max_coherence', 0):.4f}</span></p>
        <p><strong>Turnos en Efecto Reflex:</strong> {results.get('summary', {}).get('reflex_count', 0)}</p>
    </div>

    <h2>Archivos</h2>
    <table>
        <tr>
            <th>Archivo</th>
            <th>Diálogos</th>
            <th>Promedio C</th>
            <th>Máximo C</th>
            <th>Efecto Reflex</th>
        </tr>
"""

    for f in results.get('files', []):
        html += f"""
        <tr>
            <td>{f.get('source_file', 'N/A')}</td>
            <td>{len(f.get('c_values', []))}</td>
            <td>{f.get('avg_c', 0):.4f}</td>
            <td>{f.get('max_c', 0):.4f}</td>
            <td>{f.get('reflex_count', 0)} turnos</td>
        </tr>
"""

    html += """
    </table>
    <footer>
        <p><em>Generado por PNLIO Framework v2.0</em></p>
    </footer>
</body>
</html>
"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"\nReporte generado: {output_path}")
    return output_path


def main():
    """Función principal."""
    print("=" * 60)
    print("PNLIO Batch Analyzer")
    print("=" * 60)

    # Inicializar analizador
    analyzer = PNLIOAnalyzer(threshold_reflex=0.75)

    if not analyzer.load_model():
        print("Error cargando modelo.")
        return

    # Verificar argumentos
    import sys
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "data/"
        print(f"\nUsando directorio por defecto: {path}")

    if os.path.isfile(path):
        results = analyze_file(path, analyzer)
        analyzer.export_results(results, "pnlio_file_result.json")
        generate_report(results, "pnlio_file_report.html")
    elif os.path.isdir(path):
        results = analyze_directory(path, analyzer)
        analyzer.export_results(results, "pnlio_batch_results.json")
        generate_report(results, "pnlio_batch_report.html")
    else:
        print(f"Error: '{path}' no existe.")
        return

    print("\nAnálisis completado.")


if __name__ == "__main__":
    main()
