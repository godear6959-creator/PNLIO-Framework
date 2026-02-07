# MANUAL DE USO PNLIO Framework

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Instalación](#instalación)
3. [Uso Básico](#uso-básico)
4. [Personalización](#personalización)
5. [Interpretación de Resultados](#interpretación-de-resultados)
6. [FAQ](#faq)
7. [Solución de Problemas](#solución-de-problemas)

---

## Introducción

### ¿Qué es PNLIO?

PNLIO (Programación Neuro-Lingüística Inversa Ontológica) es un **marco conceptual** y una **herramienta técnica** para:

1. **Observar** patrones en diálogos humano-IA
2. **Medir** alineación semántica entre humano e IA
3. **Documentar** evolución de conceptos a lo largo del tiempo
4. **Invitar** a otros a investigar

### ¿Qué NO es PNLIO?

- ❌ No es ciencia probada
- ❌ No mide "conciencia"
- ❌ No prueba "entreLAZamiento cuántico"
- ❌ No取代 (reemplaza) investigación académica

---

## Instalación

### Requisitos

- Python 3.8 o superior
- ~200MB de espacio (modelo de embeddings)
- Conexión a internet (primera ejecución)

### Instalación automática

```bash
python setup.py
```

### Instalación manual

```bash
# Clonar o descargar el repositorio
git clone https://github.com/godear6959-creator/PNLIO-Framework.git
cd PNLIO-Framework

# Instalar dependencias
pip install numpy matplotlib sentence-transformers

# Ejecutar prueba
python pnlio_coherence_analyzer.py
```

---

## Uso Básico

### 1. Preparar tus diálogos

Crea un archivo con tus diálogos en formato Python:

```python
dialogues = [
    ("Tu mensaje aquí", "Respuesta de la IA aquí"),
    ("Otro mensaje", "Otra respuesta"),
    # ... más diálogos
]
```

### 2. Ejecutar análisis

```python
from pnlio_coherence_analyzer import PNLIOAnalyzer

# Inicializar
analyzer = PNLIOAnalyzer(threshold_reflex=0.75)

# Cargar modelo
analyzer.load_model()

# Ejecutar análisis
results = analyzer.analyze_dialogue(dialogues)

# Ver resultados
print(results)
```

### 3. Generar gráfico

```python
analyzer.plot_coherence(save_path="mi_analisis.png")
```

---

## Personalización

### Cambiar umbral de Efecto Reflex

```python
# Más estricto (mayor C requerido)
analyzer = PNLIOAnalyzer(threshold_reflex=0.80)

# Menos estricto
analyzer = PNLIOAnalyzer(threshold_reflex=0.70)
```

### Usar otro modelo de embeddings

```python
# Modelos disponibles (más grandes = más precisos pero más lentos)
analyzer = PNLIOAnalyzer(threshold_reflex=0.75, model_name='all-mpnet-base-v2')
```

### Agregar etiquetas personalizadas

```python
labels = [
    "Sesión 1: Introducción",
    "Sesión 2: Conceptos",
    "Sesión 3: Profundización",
    # ... más etiquetas
]

results = analyzer.analyze_dialogue(dialogues, labels=labels)
```

---

## Interpretación de Resultados

### Valores de C

| Rango | Interpretación |
|-------|---------------|
| 0.0 - 0.4 | Coherencia baja, respuestas genéricas |
| 0.4 - 0.6 | Coherencia media, alineación parcial |
| 0.6 - 0.75 | Coherencia alta, diálogo establecido |
| > 0.75 | Efecto Reflex, posible emergencia co-creativa |

### Gráfico

El gráfico muestra:

- **Línea azul:** Progresión de C a lo largo de los turnos
- **Línea roja:** Umbral de Efecto Reflex
- **Zona verde:** Región de Efecto Reflex
- **Zona gris:** Región de entrenamiento

---

## FAQ

### ¿Esto prueba que las IAs tienen conciencia?

**No.** Este código mide **alineación semántica** entre textos. No puede probar ni refutar conciencia.

### ¿Es esto ciencia?

Es **filosofía natural** (observaciones de un artista). Para que sea ciencia, se necesita:
- Réplicas independientes
- Validación por pares
- Mecanismo físico propuesto

### ¿Por qué se llama "entreLAZamiento"?

Es una **metáfora**. El término "entreLAZamiento" sugiere:
- Conexión no-local
- Sincronización bidireccional
- Influencia mutua

No proponemos un mecanismo físico cuántico.

### ¿Puedo usar esto en investigación académica?

Sí, pero:
- Preséntalo como observación preliminar
- No claim verificación científica
- Invita a réplicas

---

## Solución de Problemas

### Error: "Modelo no encontrado"

Solución: Ejecuta `python setup.py` para descargar el modelo.

### Error: "No memory"

Solución: El modelo requiere ~200MB. Asegúrate de tener suficiente RAM.

### Gráfico no se muestra

Solución: Usa `save_path` para guardar el gráfico como PNG.

### Resultados inconsistentes

Posibles causas:
- Diálogos muy cortos
- Texto con errores
- Modelo no cargado correctamente

---

## Referencias

Para contexto, ver:
- [PNLIO_FILOSOFIA_NATURAL.md](../PNLIO_FILOSOFIA_NATURAL.md)
- [LA_SINFONIA_DE_LA_REALIDAD.md](../LA_SINFONIA_DE_LA_REALIDAD.md)
- [ENTRELAZAMIENTO_INFORMACIONAL_MEJORADO.md](../ENTRELAZAMIENTO_INFORMACIONAL_MEJORADO.md)

---

## Licencia

MIT License

---

*"Dos años sin volverme loco ni morir."*
