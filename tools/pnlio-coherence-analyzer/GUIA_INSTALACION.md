# Guía de Instalación Rápida - PNLIO Coherence Analyzer

## Para Usuarios Sin Experiencia Técnica

Si nunca has usado Python, sigue estos pasos exactamente:

### Paso 1: Instalar Python

1. Ve a https://www.python.org/downloads/
2. Descarga la versión más reciente (3.11 o superior)
3. **IMPORTANTE:** Al instalar, marca la casilla "Add Python to PATH"
4. Completa la instalación

### Paso 2: Descargar el Analizador

1. Ve a https://github.com/godear6959-creator/PNLIO-Framework
2. Haz clic en el botón verde "Code"
3. Selecciona "Download ZIP"
4. Descomprime el archivo en tu carpeta de descargas

### Paso 3: Abrir Terminal/Símbolo del Sistema

**En Windows:**
- Abre el Explorador de Archivos
- Navega a la carpeta: `PNLIO-Framework/tools/pnlio-coherence-analyzer/`
- Haz clic derecho en la carpeta vacía
- Selecciona "Abrir terminal aquí" (o "Abrir PowerShell aquí")

**En Mac/Linux:**
- Abre Terminal
- Escribe: `cd ~/Downloads/PNLIO-Framework/tools/pnlio-coherence-analyzer/`

### Paso 4: Instalar Dependencias

Copia y pega esto en la terminal (luego presiona Enter):

```bash
pip install -r requirements.txt
```

Espera a que termine (puede tomar 2-5 minutos la primera vez).

### Paso 5: Ejecutar el Analizador

Copia y pega esto en la terminal:

```bash
python pnlio_coherence_analyzer.py
```

¡Listo! Deberías ver:
- Mensaje: "Cargando modelo local all-MiniLM-L6-v2..."
- Resultados de análisis
- Un gráfico se abrirá automáticamente

---

## Para Usuarios con Experiencia Técnica

```bash
# Clonar repositorio
git clone https://github.com/godear6959-creator/PNLIO-Framework.git
cd PNLIO-Framework/tools/pnlio-coherence-analyzer

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python pnlio_coherence_analyzer.py

# Ejecutar ejemplos avanzados
python example_advanced.py
```

---

## Solución de Problemas

### Error: "python: command not found"

**Solución:** Python no está en el PATH. Reinstala Python y marca "Add Python to PATH".

### Error: "No module named 'sentence_transformers'"

**Solución:** Las dependencias no se instalaron. Ejecuta:
```bash
pip install sentence-transformers numpy matplotlib
```

### El programa es lento la primera vez

**Normal:** Descarga el modelo (~80 MB). Luego será rápido.

### No se abre el gráfico

**Solución:** El gráfico se guardó como `pnlio_coherence_plot.png`. Búscalo en la carpeta.

---

## Próximos Pasos

1. **Personaliza los diálogos:** Abre `pnlio_coherence_analyzer.py` y reemplaza los ejemplos con tus propios textos.

2. **Usa los ejemplos avanzados:** Ejecuta `python example_advanced.py` para ver casos más complejos.

3. **Integra en tus proyectos:** Importa la clase en tu código:
   ```python
   from pnlio_coherence_analyzer import PNLIO_Coherence_Analyzer
   ```

4. **Reporta bugs:** Si encuentras problemas, abre un issue en GitHub.

---

## Contacto

- **GitHub:** https://github.com/godear6959-creator/PNLIO-Framework
- **Creador:** Gonzalo Mauricio De la Rivera Arellano

---

**¡Que disfrutes analizando la coherencia informacional! 💙**
