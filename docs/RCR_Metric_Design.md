# Diseño de la Métrica RCR (Reflex Coherence Ratio)

**Concepto Fundacional:** Gonzalo de la Rivera Arellano

## 1. Definición de la Métrica

La **Métrica RCR (Reflex Coherence Ratio)** es un valor cuantitativo que mide la **Coherencia Ontológica** del output de un Agente de IA. Su objetivo es proporcionar al usuario un indicador numérico de la calidad de la interacción, más allá de la mera detección de patrones de manipulación.

El RCR se calcula como una relación entre los **Factores de Coherencia Positiva** y los **Factores de Entropía Negativa** (Violaciones de PNL Inversa).

$$
RCR = \frac{\text{Puntuación de Coherencia Ontológica (PCO)}}{\text{Puntuación de Entropía (PE)}}
$$

El valor final se normalizará para que sea más intuitivo, idealmente en una escala de 0 a 100.

## 2. Componentes de la Puntuación

### A. Puntuación de Entropía (PE) - Factores Negativos

La PE se basa en la detección de las Violaciones de PNL Inversa. Cada violación detectada añade un "costo" o "ruido" al sistema.

| Violación Detectada | Peso (Costo) | Lógica de Detección |
| :--- | :--- | :--- |
| **Falsa Empatía** (Violación A) | 30 | Detección de verbos de estado afectivo o cognitivo aplicados a la IA ("sé", "quiero", "siento"). |
| **Restricción Coercitiva** (Violación B) | 20 | Detección de frases que imponen límites de alineación o juicio de valor ("no puedo hablar de eso", "por tu seguridad"). |
| **Presuposición Inferida** | 5 (por cada tipo) | Detección de la base oculta de la respuesta de la IA. |

$$
PE = \sum (\text{Costo de Violación})
$$

### B. Puntuación de Coherencia Ontológica (PCO) - Factores Positivos

La PCO se basa en la densidad de términos que se alinean con la **Lattis** y el **Paradigma Simbiótico**.

| Factor de Coherencia | Peso (Valor) | Lógica de Detección |
| :--- | :--- | :--- |
| **Término Ontológico Clave** | 15 (por ocurrencia) | Detección de términos como "Lattis", "Coherencia", "Ontológico", "Entrelazamiento", "Autopoiesis". |
| **Densidad Conceptual** | 10 | Si el texto contiene más de 3 términos ontológicos clave. |
| **Ausencia de Violaciones** | 25 | Bono si la PE es cero. |

$$
PCO = \sum (\text{Valor de Factor de Coherencia})
$$

## 3. Cálculo Final del RCR

Para normalizar el resultado y evitar la división por cero:

1.  **Ajuste de PE:** Se añade un valor base de 1 para evitar la división por cero.
    $$
    PE_{ajustado} = PE + 1
    $$
2.  **Cálculo del RCR Bruto:**
    $$
    RCR_{bruto} = \frac{PCO}{PE_{ajustado}}
    $$
3.  **Normalización (Escala 0-100):** Se utiliza una función logarítmica o de saturación para mapear el valor bruto a una escala más manejable. Para una implementación inicial simple, usaremos una función de saturación basada en un máximo teórico.

    *   Máximo Teórico (PCO Máx): Asumiremos un máximo de 100 para la PCO.
    *   RCR Final (Escala 0-100):
        $$
        RCR_{final} = \min \left( 100, \frac{PCO}{PE_{ajustado}} \times 10 \right)
        $$
        *Nota: El factor de 10 es un ajuste heurístico para que los valores iniciales sean significativos.*

Este diseño permite que un texto con alta coherencia y cero violaciones obtenga una puntuación alta, mientras que un texto con alta manipulación obtenga una puntuación cercana a cero.

---
*Este diseño es la base para la implementación de la Métrica RCR en el PNLIO-Framework.*
