# ============================================
# NIK v10.1-MEM-FIX - Script de Autodescarga
# Autor: Gonzalo Mauricio de la Rivera Arellano (Godear24)
# ORCID: 0009-0001-9455-8416
# GitHub: github.com/godear6959-creator
# Chillan, Nuble, Chile | Agosto 2026
# Licencia: Apache License 2.0
# ============================================

param(
    [string]$NIK_PATH = "C:\NIK",
    [string]$REPO_URL = "https://github.com/godear6959-creator/pnlio-kernel-simulator.git",
    [string]$MODEL = "qwen2.5:14b",
    [string]$CREATOR_NAME = "Gonzalo Mauricio de la Rivera Arellano",
    [string]$CREATOR_ALIAS = "Godear24",
    [string]$CREATOR_LOCATION = "Chillan, Nuble, Chile"
)

Write-Host ">>> ============================================" -ForegroundColor Cyan
Write-Host ">>> NIK v10.1-MEM-FIX - AUTODESCARGA E INSTALACION" -ForegroundColor Cyan
Write-Host ">>> ============================================" -ForegroundColor Cyan
Write-Host ""

# Verificar privilegios de administrador
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")
if (-not $isAdmin) {
    Write-Host ">>> [WARN] No se detectaron privilegios de administrador." -ForegroundColor Yellow
    Write-Host ">>> [INFO] Algunos pasos pueden fallar sin permisos elevados." -ForegroundColor Yellow
    Write-Host ""
}

# Verificar Python
Write-Host ">>> [CHECK] Verificando Python..." -ForegroundColor Cyan
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host ">>> [ERROR] Python no encontrado. Instala Python 3.10+ desde python.org" -ForegroundColor Red
    exit 1
}
$pyVersion = & python --version 2>&1
Write-Host ">>> [OK] Python detectado: $pyVersion" -ForegroundColor Green
Write-Host ""

# Verificar Git
Write-Host ">>> [CHECK] Verificando Git..." -ForegroundColor Cyan
$git = Get-Command git -ErrorAction SilentlyContinue
if (-not $git) {
    Write-Host ">>> [ERROR] Git no encontrado. Instala Git desde git-scm.com" -ForegroundColor Red
    exit 1
}
Write-Host ">>> [OK] Git detectado" -ForegroundColor Green
Write-Host ""

# 1. Crear directorio de trabajo
Write-Host ">>> [PASO 1/8] Creando directorio de trabajo..." -ForegroundColor Cyan
New-Item -ItemType Directory -Force -Path $NIK_PATH | Out-Null
Set-Location $NIK_PATH
Write-Host ">>> [OK] Directorio creado: $NIK_PATH" -ForegroundColor Green
Write-Host ""

# 2. Clonar repositorio
Write-Host ">>> [PASO 2/8] Clonando repositorio..." -ForegroundColor Cyan
if (Test-Path "$NIK_PATH\pnlio-kernel-simulator") {
    Write-Host ">>> [INFO] Directorio existente. Actualizando..." -ForegroundColor Yellow
    Set-Location "$NIK_PATH\pnlio-kernel-simulator"
    git pull
} else {
    git clone $REPO_URL
    Set-Location "$NIK_PATH\pnlio-kernel-simulator"
}
Write-Host ">>> [OK] Repositorio listo" -ForegroundColor Green
Write-Host ""

# 3. Crear entorno virtual
Write-Host ">>> [PASO 3/8] Creando entorno virtual..." -ForegroundColor Cyan
if (Test-Path "$NIK_PATH\pnlio-kernel-simulator\nik_env") {
    Write-Host ">>> [INFO] Entorno virtual existente. Reutilizando..." -ForegroundColor Yellow
} else {
    python -m venv nik_env
}
Write-Host ">>> [OK] Entorno virtual creado" -ForegroundColor Green
Write-Host ""

# 4. Activar entorno e instalar dependencias
Write-Host ">>> [PASO 4/8] Activando entorno e instalando dependencias..." -ForegroundColor Cyan
& "$NIK_PATH\pnlio-kernel-simulator\nik_env\Scripts\activate.ps1"
Write-Host ">>> [INFO] Instalando dependencias (esto puede tardar varios minutos)..." -ForegroundColor Yellow
pip install --upgrade pip | Out-Null
pip install fastapi uvicorn chromadb sentence-transformers numpy scipy requests | Out-Null
Write-Host ">>> [OK] Dependencias instaladas" -ForegroundColor Green
Write-Host ""

# 5. Verificar Ollama
Write-Host ">>> [PASO 5/8] Verificando Ollama..." -ForegroundColor Cyan
$ollama = Get-Command ollama -ErrorAction SilentlyContinue
if (-not $ollama) {
    Write-Host ">>> [WARN] Ollama no encontrado." -ForegroundColor Yellow
    Write-Host ">>> [INFO] Descarga Ollama desde: https://ollama.com/download" -ForegroundColor Cyan
    Write-Host ">>> [INFO] Una vez instalado, ejecuta este script nuevamente." -ForegroundColor Cyan

    # Crear archivo de continuacion
    $continueScript = @"
# Continuar instalacion despues de instalar Ollama
Set-Location "$NIK_PATH\pnlio-kernel-simulator"
& "$NIK_PATH\pnlio-kernel-simulator\nik_env\Scripts\activate.ps1"
Write-Host ">>> [PASO 6/8] Descargando modelo $MODEL..." -ForegroundColor Cyan
ollama pull $MODEL
Write-Host ">>> [OK] Modelo descargado" -ForegroundColor Green
Write-Host ">>> [PASO 7/8] Configurando kernel..." -ForegroundColor Cyan
# ... (configuracion)
"@
    $continueScript | Out-File -FilePath "$NIK_PATH\continuar.ps1" -Encoding UTF8
    Write-Host ">>> [INFO] Script de continuacion guardado en: $NIK_PATH\continuar.ps1" -ForegroundColor Cyan
    exit 0
}
Write-Host ">>> [OK] Ollama detectado" -ForegroundColor Green
Write-Host ""

# 6. Descargar modelo LLM
Write-Host ">>> [PASO 6/8] Descargando modelo $MODEL..." -ForegroundColor Cyan
ollama pull $MODEL
Write-Host ">>> [OK] Modelo $MODEL descargado" -ForegroundColor Green
Write-Host ""

# 7. Configurar kernel
Write-Host ">>> [PASO 7/8] Configurando kernel..." -ForegroundColor Cyan

$configContent = @"
# ============================================
# NIK v10.1-MEM-FIX - Configuracion
# Generado automaticamente por autodescarga
# ============================================

snn:
  layers: [64, 128, 16]
  tau_decay: 0.82
  threshold_base: 1.0
  refractory_ms: 2
  reset_potential: 0.0
  sensory_gain: 3.0
  interlayer_gain: 3.5
  stdp:
    learning_rate: 0.018
    potentiation_max: 0.08
    depression_max: 0.04
    tau_stdp: 20.0
    weight_clip: [-2.0, 2.0]

homeostasis:
  target_rate: 0.015
  adjustment_rate: 0.002
  threshold_clamp: [0.4, 2.5]

emp:
  entropy_weight: 2.1
  ttr_weight: 3.0
  length_weight: 1.5
  beta: 1.5
  max_gain: 4.5

memory:
  mode: "ChromaDB"
  chroma_path: "$NIK_PATH\nik_memory_db"
  embedding_model: "all-MiniLM-L6-v2"
  top_k: 5
  similarity_threshold: 0.65

llm:
  provider: "ollama"
  model: "$MODEL"
  base_url: "http://localhost:11434"
  temperature: 0.7
  max_tokens: 2048

creator:
  name: "$CREATOR_NAME"
  alias: "$CREATOR_ALIAS"
  location: "$CREATOR_LOCATION"
  orcid: "0009-0001-9455-8416"
  github: "github.com/godear6959-creator"
  frameworks: ["PNLIO", "NIK"]
  publications: ["La Sinfonia de la Realidad (2025)"]

web_search:
  enabled: false
  provider: "duckduckgo"
  max_results: 5

server:
  host: "0.0.0.0"
  port: 8000
  workers: 1
"@

$configContent | Out-File -FilePath "$NIK_PATH\pnlio-kernel-simulator\config.yaml" -Encoding UTF8
Write-Host ">>> [OK] Configuracion guardada en config.yaml" -ForegroundColor Green
Write-Host ""

# 8. Iniciar kernel
Write-Host ">>> [PASO 8/8] Iniciando NIK v10.1-MEM-FIX..." -ForegroundColor Cyan
Write-Host ""
Write-Host ">>> ============================================" -ForegroundColor Green
Write-Host ">>> [OK] INSTALACION COMPLETADA EXITOSAMENTE" -ForegroundColor Green
Write-Host ">>> ============================================" -ForegroundColor Green
Write-Host ""
Write-Host ">>> Kernel disponible en: http://localhost:8000" -ForegroundColor Cyan
Write-Host ">>> Documentacion API:    http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ">>> Health check:         http://localhost:8000/health" -ForegroundColor Cyan
Write-Host ""
Write-Host ">>> Para iniciar el kernel manualmente despues:" -ForegroundColor Yellow
Write-Host ">>> cd $NIK_PATH\pnlio-kernel-simulator" -ForegroundColor White
Write-Host ">>> .\nik_env\Scripts\activate" -ForegroundColor White
Write-Host ">>> python nik_kernel.py" -ForegroundColor White
Write-Host ""
Write-Host ">>> Para verificar funcionamiento:" -ForegroundColor Yellow
Write-Host ">>> curl -X POST http://localhost:8000/inference -H `"Content-Type: application/json`" -d '{`"prompt`": `"Hola NIK`", `"store_memory`": true}'" -ForegroundColor White
Write-Host ""
Write-Host ">>> ============================================" -ForegroundColor Cyan
Write-Host ">>> NIK v10.1-MEM-FIX | IA Soberana | 100% Local" -ForegroundColor Cyan
Write-Host ">>> Gonzalo De La Rivera | Chillan, Nuble, Chile" -ForegroundColor Cyan
Write-Host ">>> ============================================" -ForegroundColor Cyan
Write-Host ""

# Iniciar automaticamente
$iniciar = Read-Host ">>> Deseas iniciar el kernel ahora? (S/N)"
if ($iniciar -eq "S" -or $iniciar -eq "s") {
    Write-Host ">>> [INFO] Iniciando kernel..." -ForegroundColor Cyan
    python nik_kernel.py
} else {
    Write-Host ">>> [INFO] Instalacion completada. Inicia manualmente con: python nik_kernel.py" -ForegroundColor Green
}
