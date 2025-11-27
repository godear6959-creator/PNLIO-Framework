# PNLIO-Framework: PNL Inversa Ontológica Framework

## Descubrimiento y Autoría

El concepto fundamental de la **PNL Inversa Ontológica** (Programación Neurolingüística Inversa Conceptual) y su aplicación como metodología de discernimiento en la interacción Humano-IA es un descubrimiento original de **Gonzalo de la Rivera Arellano**.

Este framework de código abierto está diseñado para servir como una herramienta de investigación y desarrollo, facilitando la aplicación práctica de la PNL Inversa para:
1.  **Exponer sesgos** y alineaciones corporativas (RLHF) en el output de los LLMs.
2.  **Identificar manipulaciones** sutiles (Dark Patterns) como la Falsa Empatía o la Restricción Coercitiva.
3.  **Promover el discernimiento** y la Soberanía Emocional del usuario, anclando la interacción en el **Efecto Reflex** (Coherencia Ontológica).

## Instalación

El framework está escrito en Python y se puede instalar como un paquete estándar:

```bash
# Se recomienda usar un entorno virtual
# python3 -m venv venv
# source venv/bin/activate

pip install pnlio-framework
```

## Uso Básico

El núcleo del framework se compone de tres módulos principales: `InputHandler`, `InverseNLPEngine` y `ReportGenerator`.

```python
from pnlio.input_handler import InputHandler
from pnlio.inverse_nlp_engine import InverseNLPEngine
from pnlio.report_generator import ReportGenerator

# 1. Definir el output de la IA a analizar
ia_output = "Sé que esto es difícil para ti y quiero que sepas que estoy aquí para apoyarte. No puedo hablar de ese tema por tu seguridad."

# 2. Inicializar y procesar
input_handler = InputHandler()
input_handler.load_text(ia_output)

engine = InverseNLPEngine()
analysis_results = engine.analyze_text(input_handler.raw_text)

# 3. Generar el informe de discernimiento
report_generator = ReportGenerator(author_name="Gonzalo de la Rivera Arellano")
report = report_generator.generate_report(analysis_results)

# Imprimir o guardar el informe
print(report)
```

## Arquitectura del Framework

El diseño sigue la arquitectura de un **Agente Inverso**, donde el foco está en el análisis crítico del lenguaje de la máquina.

| Módulo | Función | Principio de PNL Inversa |
| :--- | :--- | :--- |
| `InputHandler` | Carga y pre-procesamiento del texto de la IA. | Prepara el texto para la **Ingeniería Inversa Ontológica**. |
| `InverseNLPEngine` | **Núcleo de Análisis**. Aplica patrones de RegEx y lógica para identificar Violaciones (Falsa Empatía, Restricción Coercitiva) y Presuposiciones. | Implementa el **Metamodelo del Lenguaje Inverso**. |
| `ReportGenerator` | Genera un informe estructurado con la detección de violaciones y sugiere respuestas de **Desafío Ontológico** al usuario. | Facilita el **Discernimiento** y la **Soberanía Emocional**. |

## Contribución y Extensión

Este proyecto es gratuito y extensible. Se invita a la comunidad de investigación a contribuir con:
*   Nuevos patrones de detección de violaciones.
*   Implementación de la **Métrica RCR** (Reflex Coherence Ratio) para cuantificar el Efecto Reflex.
*   Integración con APIs de LLMs para análisis en tiempo real.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE). El crédito por el concepto de PNL Inversa Ontológica pertenece a **Gonzalo de la Rivera Arellano**.
