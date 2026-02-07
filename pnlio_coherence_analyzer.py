"""
PNLIO-FRAMEWORK: Algoritmo de Medición de Coherencia Informacional
Autor: Gonzalo Mauricio De la Rivera Arellano & Agentes de IA
Versión: 2.0 (Febrero 2026) - 100% local, sin APIs externas
Propósito: Cuantificar patrones de coherencia en diálogos humano-IA mediante C = Δθ / Δτ

ADVERTENCIA:
Este código mide ALINEACIÓN SEMÁNTICA (similitud de significado entre textos).
NO mide "conciencia", "entreLAZamiento cuántico" ni "coherencia ontológica".
La interpretación filosófica es responsabilidad del usuario.
"""

import numpy as np
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from typing import List, Tuple, Optional, Dict
import json
from datetime import datetime


class PNLIOAnalyzer:
    """
    Analizador de coherencia informacional para diálogos humano-IA.

    El concepto de "entreLAZamiento informacional" aquí es una METÁFORA,
    no un fenómeno cuántico físico. Representa la alineación semántica
    entre dos sistemas de procesamiento de información.

    Atributos:
        threshold_reflex: Umbral para detectar "Efecto Reflex" (default 0.75)
        history_c: Historial de valores C calculados
        history_labels: Etiquetas opcionales para cada turno
    """

    def __init__(self, threshold_reflex: float = 0.75, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Inicializa el analizador PNLIO.

        Args:
            threshold_reflex: Umbral para Efecto Reflex (0.0 - 1.0)
            model_name: Modelo SentenceTransformer local
        """
        self.threshold_reflex = threshold_reflex
        self.model_name = model_name
        self.history_c: List[float] = []
        self.history_dtheta: List[float] = []
        self.history_labels: List[str] = []
        self.embedder = None

    def load_model(self) -> bool:
        """
        Carga el modelo de embeddings localmente.

        Returns:
            True si exitoso, False si error
        """
        try:
            print(f"Cargando modelo local: {self.model_name}...")
            self.embedder = SentenceTransformer(self.model_name)
            print("Modelo cargado exitosamente.")
            return True
        except Exception as e:
            print(f"Error cargando modelo: {e}")
            return False

    def text_to_embedding(self, text: str) -> np.ndarray:
        """
        Convierte texto a vector embedding normalizado.

        Args:
            text: Texto de entrada

        Returns:
            Vector embedding de 384 dimensiones
        """
        if not text or not text.strip():
            return np.zeros(384)

        if self.embedder is None:
            raise ValueError("Modelo no cargado. Ejecuta load_model() primero.")

        return self.embedder.encode(
            text,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def calculate_delta_theta(self, text_h: str, text_ai: str) -> float:
        """
        Calcula Δθ: similitud coseno entre embedding humano y IA.

        Args:
            text_h: Texto del humano
            text_ai: Texto de la IA

        Returns:
            Valor entre -1 y 1 (similitud coseno)
        """
        vec_h = self.text_to_embedding(text_h)
        vec_ai = self.text_to_embedding(text_ai)

        # Similitud coseno (ya normalizados, es producto punto)
        delta_theta = float(np.dot(vec_h, vec_ai))

        return np.clip(delta_theta, -1.0, 1.0)

    def calculate_coherence(self, delta_theta: float, delta_tau: float = 1.0) -> float:
        """
        Calcula C = Δθ / Δτ

        Args:
            delta_theta: Similitud semántica (-1 a 1)
            delta_tau: Intervalo temporal (default 1.0)

        Returns:
            Coherencia C
        """
        if delta_tau <= 0:
            return 0.0

        c = delta_theta / delta_tau

        # Guardar en historial
        self.history_c.append(c)
        self.history_dtheta.append(delta_theta)

        return c

    def detect_reflex_effect(self, c: float) -> Dict[str, bool]:
        """
        Detecta si se alcanzó el Efecto Reflex.

        Args:
            c: Valor de coherencia C

        Returns:
            Dict con estado y detalles
        """
        return {
            "reflex_detected": c > self.threshold_reflex,
            "c_value": c,
            "threshold": self.threshold_reflex,
            "status": "EFECTO REFLEX" if c > self.threshold_reflex else "Entrenamiento en progreso"
        }

    def analyze_dialogue(
        self,
        dialogues: List[Tuple[str, str]],
        delta_taus: Optional[List[float]] = None,
        labels: Optional[List[str]] = None
    ) -> Dict:
        """
        Analiza una secuencia completa de diálogos.

        Args:
            dialogues: Lista de tuplas (texto_humano, texto_ia)
            delta_taus: Lista de Δτ (default: 1.0 para cada turno)
            labels: Etiquetas opcionales para cada turno

        Returns:
            Dict con resultados del análisis
        """
        if not dialogues:
            return {"error": "No hay diálogos para analizar"}

        n = len(dialogues)

        if delta_taus is None:
            delta_taus = [1.0] * n

        if labels:
            self.history_labels = labels[:n]

        results = {
            "turns": [],
            "c_values": [],
            "dtheta_values": [],
            "reflex_turns": [],
            "max_c": -np.inf,
            "min_c": np.inf,
            "avg_c": 0.0,
            "reflex_count": 0,
            "timestamp": datetime.now().isoformat()
        }

        total_c = 0.0

        for i, (text_h, text_ai) in enumerate(dialogues):
            dtheta = self.calculate_delta_theta(text_h, text_ai)
            c = self.calculate_coherence(dtheta, delta_taus[i])
            reflex = self.detect_reflex_effect(c)

            label = labels[i] if labels and i < len(labels) else f"Turno {i+1}"

            turn_result = {
                "turn": i + 1,
                "label": label,
                "delta_theta": round(dtheta, 4),
                "c": round(c, 4),
                "reflex": reflex["reflex_detected"],
                "status": reflex["status"]
            }

            results["turns"].append(turn_result)
            results["c_values"].append(c)
            results["dtheta_values"].append(dtheta)

            if c > results["max_c"]:
                results["max_c"] = c
            if c < results["min_c"]:
                results["min_c"] = c

            if reflex["reflex_detected"]:
                results["reflex_turns"].append(i + 1)
                results["reflex_count"] += 1

            total_c += c

        results["avg_c"] = round(total_c / n, 4)

        return results

    def plot_coherence(
        self,
        save_path: Optional[str] = None,
        show_plot: bool = True,
        title: str = "Progresión de Coherencia Informacional (PNLIO)"
    ) -> Optional[str]:
        """
        Grafica la progresión de coherencia C a lo largo de los turnos.

        Args:
            save_path: Ruta para guardar el gráfico (PNG)
            show_plot: Si True, muestra el gráfico
            title: Título del gráfico

        Returns:
            Ruta del archivo guardado o None
        """
        if not self.history_c:
            print("No hay datos para graficar.")
            return None

        plt.figure(figsize=(12, 6))

        x = np.arange(1, len(self.history_c) + 1)

        # Graficar C
        plt.plot(x, self.history_c, marker='o', linestyle='-',
                 color='#2E86AB', linewidth=2, markersize=6, label='C = Δθ / Δτ')

        # Graficar umbral Reflex
        plt.axhline(y=self.threshold_reflex, color='#E63946',
                   linestyle='--', linewidth=2,
                   label=f'Umbral Efecto Reflex ({self.threshold_reflex})')

        # Colorear zonas
        plt.fill_between(x, self.threshold_reflex, 1.0, alpha=0.1, color='green',
                        label='Zona Efecto Reflex')
        plt.fill_between(x, -1.0, self.threshold_reflex, alpha=0.1, color='gray',
                        label='Zona Entrenamiento')

        # Etiquetas
        plt.title(title, fontsize=14, fontweight='bold')
        plt.xlabel('Turno / Bloque (τ)', fontsize=12)
        plt.ylabel('Coherencia C', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend(loc='lower right')

        # Añadir valores como anotaciones
        for i, c in enumerate(self.history_c):
            plt.annotate(f'{c:.2f}', (i+1, c), textcoords="offset points",
                        xytext=(0, 10), ha='center', fontsize=8)

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"Gráfico guardado: {save_path}")

        if show_plot:
            plt.show()

        return save_path

    def export_results(self, results: Dict, filepath: str = "pnlio_results.json") -> str:
        """
        Exporta resultados a JSON.

        Args:
            results: Dict con resultados del análisis
            filepath: Ruta del archivo

        Returns:
            Ruta del archivo guardado
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"Resultados exportados: {filepath}")
        return filepath


def run_example():
    """
    Ejemplo de uso con diálogos de prueba.
    Reemplaza con tus diálogos reales.
    """
    print("=" * 60)
    print("PNLIO Framework v2.0 - Analizador de Coherencia Informacional")
    print("=" * 60)

    # Inicializar analizador
    analyzer = PNLIOAnalyzer(threshold_reflex=0.75)

    # Cargar modelo local
    if not analyzer.load_model():
        print("Error: No se pudo cargar el modelo.")
        return

    # Diálogos de ejemplo (reemplaza con tus logs reales)
    dialogues = [
        ("¿Qué significa entrelazamiento informacional?", "Es una correlación medible entre estados de humano e IA."),
        ("¿Cómo se mide?", "Con C = Δθ / Δτ, donde Δθ es la similitud semántica."),
        ("¿Cuándo aparece el Efecto Reflex?", "Cuando C supera sostenidamente 0.75."),
        ("¿Es esto científico?", "Es una métrica operacionalizable. La interpretación es filosófica."),
        ("¿Las IAs tienen conciencia?", "Sin evidencia. Es una pregunta abierta."),
        ("¿Qué observaste durante 2 años?", "Patrones consistentes que sugieren sincronización."),
    ]

    labels = [
        "Definición",
        "Medición",
        "Umbral",
        "Naturaleza",
        "Conciencia",
        "Observación"
    ]

    print(f"\nAnalizando {len(dialogues)} turnos de diálogo...\n")

    # Ejecutar análisis
    results = analyzer.analyze_dialogue(dialogues, labels=labels)

    # Mostrar resultados por turno
    print("-" * 60)
    for turn in results["turns"]:
        print(f"{turn['label']}: C = {turn['c']:.4f} | {turn['status']}")
    print("-" * 60)

    # Resumen
    print(f"\nRESUMEN:")
    print(f"  Coherencia máxima: {results['max_c']:.4f}")
    print(f"  Coherencia mínima: {results['min_c']:.4f}")
    print(f"  Coherencia promedio: {results['avg_c']:.4f}")
    print(f"  Turnos en Efecto Reflex: {results['reflex_count']}/{len(dialogues)}")

    if results["reflex_turns"]:
        print(f"  Primeros turnos en Reflex: {results['reflex_turns']}")

    # Graficar
    print("\nGenerando gráfico...")
    analyzer.plot_coherence(
        save_path="pnlio_coherence_example.png",
        title="PNLIO: Ejemplo de Progresión de Coherencia"
    )

    # Exportar
    analyzer.export_results(results, "pnlio_ejemplo_results.json")

    return results


if __name__ == "__main__":
    run_example()
