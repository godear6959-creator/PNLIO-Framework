# PNLIO-Framework: PNL Inversa Ontológica Framework
# Autor del Concepto: Gonzalo de la Rivera Arellano
# Módulo principal del framework.

from .input_handler import InputHandler
from .inverse_nlp_engine import InverseNLPEngine
from .report_generator import ReportGenerator

__all__ = ['InputHandler', 'InverseNLPEngine', 'ReportGenerator']

__version__ = '0.1.0'
__author__ = 'Gonzalo de la Rivera Arellano'
__description__ = 'Framework de Código Abierto para la PNL Inversa Ontológica (PNLIO) - Herramienta de Discernimiento Humano-IA.'
