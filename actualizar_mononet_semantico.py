
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONONET - DICCIONARIO SEMÁNTICO PNLIO
Genera un archivo JSON para reconocimiento de conceptos.
Solo biblioteca estándar. Sin Internet ni API.
"""

import json
import hashlib
from pathlib import Path

OUTPUT = Path("pnlio_semantic_knowledge.json")


def build_knowledge():

    concepts = [
        {
            "id": "PNLIO",
            "term": "PNLIO",
            "aliases": [
                "kernel PNLIO",
                "framework PNLIO",
                "ecosistema PNLIO"
            ],
            "keywords": [
                "inteligencia artificial",
                "orquestación",
                "memoria",
                "continuidad",
                "contexto"
            ],
            "definition": (
                "Arquitectura experimental de orquestación "
                "de inteligencia artificial local basada en "
                "memoria, continuidad y contexto."
            )
        },
        {
            "id": "SOLEDAD",
            "term": "SOLEDAD",
            "aliases": [
                "kernel SOLEDAD",
                "SOLEDAD v7.1.1",
                "asistente SOLEDAD"
            ],
            "keywords": [
                "asistente local",
                "documentos",
                "RAG",
                "Phi-3",
                "Ollama",
                "ChromaDB"
            ],
            "definition": (
                "Asistente local documentado en PNLIO v7.1.1, "
                "con recuperación documental RAG."
            )
        },
        {
            "id": "RAG",
            "term": "RAG",
            "aliases": [
                "Retrieval Augmented Generation",
                "recuperación aumentada",
                "generación aumentada por recuperación"
            ],
            "keywords": [
                "documentos",
                "búsqueda",
                "recuperación",
                "contexto"
            ],
            "definition": (
                "Técnica que recupera información de documentos "
                "y la utiliza como contexto para generar respuestas."
            )
        },
        {
            "id": "MEMORIA",
            "term": "Memoria",
            "aliases": [
                "memoria persistente",
                "memoria explícita",
                "memoria contextual"
            ],
            "keywords": [
                "guardar",
                "recordar",
                "recuperar",
                "historial"
            ],
            "definition": (
                "Almacenamiento de información para su consulta "
                "y reutilización posterior."
            )
        },
        {
            "id": "CONTINUIDAD",
            "term": "Continuidad",
            "aliases": [
                "continuidad episódica",
                "continuidad contextual"
            ],
            "keywords": [
                "episodios",
                "sesiones",
                "historial",
                "interacciones anteriores"
            ],
            "definition": (
                "Conservación de referencias a interacciones "
                "anteriores para mantener seguimiento."
            )
        },
        {
            "id": "CONTEXTO",
            "term": "Contexto",
            "aliases": [
                "contexto conversacional",
                "contexto de consulta"
            ],
            "keywords": [
                "antecedentes",
                "consulta",
                "información relevante"
            ],
            "definition": (
                "Información pertinente utilizada para interpretar "
                "una consulta y elaborar una respuesta."
            )
        },
        {
            "id": "OLLAMA",
            "term": "Ollama",
            "aliases": [
                "runtime local",
                "servidor de modelos local"
            ],
            "keywords": [
                "inferencia",
                "modelos",
                "LLM"
            ],
            "definition": (
                "Herramienta para ejecutar modelos de lenguaje "
                "en un equipo local."
            )
        },
        {
            "id": "PHI3",
            "term": "Phi-3",
            "aliases": [
                "phi3",
                "Phi 3",
                "phi-3"
            ],
            "keywords": [
                "modelo de lenguaje",
                "LLM",
                "inferencia local"
            ],
            "definition": (
                "Familia de modelos de lenguaje de Microsoft."
            )
        },
        {
            "id": "CHROMADB",
            "term": "ChromaDB",
            "aliases": [
                "Chroma",
                "base vectorial Chroma"
            ],
            "keywords": [
                "vectores",
                "embeddings",
                "colecciones",
                "búsqueda semántica"
            ],
            "definition": (
                "Base de datos vectorial utilizada para almacenar "
                "y consultar representaciones de información."
            )
        },
        {
            "id": "LATTIS",
            "term": "LATTIS",
            "aliases": [
                "módulo LATTIS",
                "extracción web"
            ],
            "keywords": [
                "requests",
                "BeautifulSoup",
                "URL",
                "extracción"
            ],
            "definition": (
                "Módulo documentado en SOLEDAD v7.1.1 para "
                "extraer contenido de páginas web cuando se solicita."
            )
        },
        {
            "id": "IA_LOCAL",
            "term": "IA local",
            "aliases": [
                "inteligencia artificial local",
                "local AI",
                "IA sin nube"
            ],
            "keywords": [
                "privacidad",
                "equipo propio",
                "modelos locales"
            ],
            "definition": (
                "Sistema de inteligencia artificial ejecutado "
                "en hardware local. No implica automáticamente "
                "ausencia de conexiones de red."
            )
        },
        {
            "id": "MONONET",
            "term": "Mononet",
            "aliases": [
                "reconocedor Mononet",
                "reconocedor de palabras"
            ],
            "keywords": [
                "vocabulario",
                "reconocimiento",
                "conceptos",
                "diccionario"
            ],
            "definition": (
                "Sistema receptor de vocabulario y relaciones "
                "conceptuales. Su comportamiento depende "
                "de su implementación."
            )
        },
        {
            "id": "RCR",
            "term": "RCR",
            "aliases": [
                "Rich Cognitive Response",
                "métrica RCR"
            ],
            "keywords": [
                "coherencia",
                "respuesta",
                "evaluación"
            ],
            "definition": (
                "Indicador experimental utilizado en algunas "
                "versiones de PNLIO. No debe considerarse "
                "validado científicamente sin pruebas independientes."
            )
        }
    ]

    relations = [
        {
            "from": "PNLIO",
            "relation": "se_fundamenta_en",
            "to": "MEMORIA"
        },
        {
            "from": "PNLIO",
            "relation": "se_fundamenta_en",
            "to": "CONTINUIDAD"
        },
        {
            "from": "PNLIO",
            "relation": "se_fundamenta_en",
            "to": "CONTEXTO"
        },
        {
            "from": "SOLEDAD",
            "relation": "utiliza",
            "to": "RAG"
        },
        {
            "from": "SOLEDAD",
            "relation": "utiliza",
            "to": "OLLAMA"
        },
        {
            "from": "SOLEDAD",
            "relation": "utiliza",
            "to": "PHI3"
        },
        {
            "from": "SOLEDAD",
            "relation": "utiliza",
            "to": "CHROMADB"
        },
        {
            "from": "SOLEDAD",
            "relation": "incluye",
            "to": "LATTIS"
        },
        {
            "from": "MONONET",
            "relation": "reconoce_vocabulario_de",
            "to": "PNLIO"
        }
    ]

    return {
        "schema": "mononet.pnlio.semantic",
        "version": "1.0",
        "language": "es-419",
        "project": {
            "name": "PNLIO",
            "author": "Gonzalo Mauricio de la Rivera Arellano",
            "principles": [
                "memoria",
                "continuidad",
                "contexto"
            ],
            "github": (
                "https://github.com/"
                "godear6959-creator/PNLIO-Framework"
            )
        },
        "concepts": concepts,
        "relations": relations,
        "recognition": {
            "ignore_case": True,
            "match_aliases": True,
            "match_keywords": True,
            "preserve_original_text": True
        },
        "notes": [
            "Diccionario semántico de apoyo para Mononet.",
            "No garantiza integración automática.",
            "Verificar las capacidades por versión.",
            "Offline no significa necesariamente "
            "que todas las funciones estén aisladas de la red."
        ]
    }


def main():

    data = build_knowledge()

    payload = json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True
    )

    data["integrity"] = {
        "algorithm": "SHA256",
        "hash": hashlib.sha256(
            payload.encode("utf-8")
        ).hexdigest()
    }

    OUTPUT.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print("MONONET - PNLIO")
    print("Diccionario generado correctamente.")
    print("Conceptos:", len(data["concepts"]))
    print("Relaciones:", len(data["relations"]))
    print("Archivo:", OUTPUT.resolve())


if __name__ == "__main__":
    main()
