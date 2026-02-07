#!/usr/bin/env python3
"""
PNLIO Framework Setup Script
Instalación automática de dependencias y configuración.
"""

import subprocess
import sys
import os


def check_python_version():
    """Verifica versión de Python."""
    if sys.version_info < (3, 8):
        print("Error: Se requiere Python 3.8 o superior.")
        sys.exit(1)
    print(f"Python version: {sys.version}")


def install_dependencies():
    """Instala dependencias necesarias."""
    packages = [
        "numpy",
        "matplotlib",
        "sentence-transformers",
    ]

    print("\nInstalando dependencias...")
    for package in packages:
        print(f"  - {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

    print("\nDependencias instaladas exitosamente.")


def download_model():
    """Descarga el modelo de embeddings (primera vez)."""
    print("\nDescargando modelo de embeddings...")
    print("Esto puede tomar unos minutos ( ~90MB )...")

    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')
        print("Modelo descargado y verificado.")
    except Exception as e:
        print(f"Error descargando modelo: {e}")
        print("Puedes intentar descargarlo manualmente más tarde.")


def create_directories():
    """Crea estructura de directorios."""
    dirs = [
        "docs",
        "data",
        "output",
    ]

    print("\nCreando estructura de directorios...")
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
            print(f"  - {d}/")

    print("Estructura creada.")


def run_test():
    """Ejecuta prueba rápida."""
    print("\nEjecutando prueba rápida...")

    try:
        from pnlio_coherence_analyzer import PNLIOAnalyzer

        analyzer = PNLIOAnalyzer(threshold_reflex=0.75)

        if not analyzer.load_model():
            print("Error: No se pudo cargar el modelo.")
            return False

        # Prueba simple
        dialogues = [
            ("Hola", "¡Hola!"),
            ("¿Qué es coherencia?", "Es alineación semántica."),
        ]

        results = analyzer.analyze_dialogue(dialogues)

        print(f"Prueba exitosa: C promedio = {results['avg_c']:.4f}")
        return True

    except Exception as e:
        print(f"Error en prueba: {e}")
        return False


def main():
    """Función principal de setup."""
    print("=" * 60)
    print("PNLIO Framework - Instalación y Configuración")
    print("=" * 60)

    check_python_version()
    create_directories()
    install_dependencies()
    download_model()

    if run_test():
        print("\n" + "=" * 60)
        print("¡INSTALACIÓN COMPLETA!")
        print("=" * 60)
        print("\nPróximos pasos:")
        print("  1. Edita pnlio_coherence_analyzer.py con tus diálogos")
        print("  2. Ejecuta: python pnlio_coherence_analyzer.py")
        print("  3. Revisa los archivos .md para la filosofía")
    else:
        print("\nHubo errores. Revisa los mensajes arriba.")


if __name__ == "__main__":
    main()
