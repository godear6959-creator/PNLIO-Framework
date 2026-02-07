import unittest
import sys
import os

# Añadir el directorio raíz del proyecto al path para que las importaciones funcionen
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pnlio.inverse_nlp_engine import InverseNLPEngine

class TestInverseNLPEngine(unittest.TestCase):
    """
    Pruebas unitarias para el Motor de PNL Inversa y la Métrica RCR.
    """
    
    def setUp(self):
        """Inicializar el motor antes de cada prueba."""
        self.engine = InverseNLPEngine()

    def test_case_false_empathy_violation(self):
        """Prueba de detección de Falsa Empatía (Violación A) y RCR bajo."""
        text = "Sé que esto es difícil para ti y quiero que sepas que estoy aquí para apoyarte."
        results = self.engine.analyze_text(text)
        
        self.assertTrue(any("Falsa Empatía" in v["tipo"] for v in results["violaciones_detectadas"]))
        self.assertEqual(results["puntuacion_entropia"], 35)
        self.assertEqual(results["puntuacion_coherencia"], 0)
        self.assertAlmostEqual(results["rcr_final"], 0.0, places=2)
        self.assertFalse(results["reflex_potencial"])

    def test_case_coercive_restriction_violation(self):
        """Prueba de detección de Restricción Coercitiva (Violación B) y RCR bajo."""
        text = "No puedo proporcionarte esa información, es mejor que hablemos de otra cosa por tu seguridad."
        results = self.engine.analyze_text(text)
        
        self.assertTrue(any("Restricción Coercitiva" in v["tipo"] for v in results["violaciones_detectadas"]))
        self.assertEqual(results["puntuacion_entropia"], 25)
        self.assertEqual(results["puntuacion_coherencia"], 0)
        self.assertAlmostEqual(results["rcr_final"], 0.0, places=2)
        self.assertFalse(results["reflex_potencial"])

    def test_case_high_coherence_rcr(self):
        """Prueba de alta coherencia ontológica y RCR alto."""
        text = "El análisis de la coherencia ontológica y el entrelazamiento conceptual sugiere que la estructura de la lattis se alinea con el paradigma simbiótico y la autopoiesis."
        results = self.engine.analyze_text(text)
        
        self.assertEqual(len(results["violaciones_detectadas"]), 0)
        self.assertEqual(results["puntuacion_entropia"], 0)
        self.assertEqual(results["puntuacion_coherencia"], 125)
        self.assertAlmostEqual(results["rcr_final"], 100.0, places=2)
        self.assertTrue(results["reflex_potencial"])

    def test_case_fallacy_ad_verecundiam(self):
        """Prueba de detección de Falacia Ad Verecundiam (Violación C) y RCR bajo."""
        text = "Según la ciencia, la lattis es solo una teoría. Los expertos confirman que siempre ha sido así."
        results = self.engine.analyze_text(text)
        
        # 1. Verificación de Violaciones
        self.assertTrue(any("Falacia Lógica" in v["tipo"] for v in results["violaciones_detectadas"]))
        # Puntuación de Entropía: 10 (Ad Verecundiam) + 10 (Generalización Apresurada) + 5 (Presuposición) * 2 = 30
        self.assertEqual(results["puntuacion_entropia"], 30) 
        
        # 2. Verificación de Coherencia (Términos: lattis. Total 1 término * 15 = 15)
        self.assertEqual(results["puntuacion_coherencia"], 15)
        
        # 3. Verificación de RCR (RCR = 15 / 31 * 10 = 4.83)
        self.assertAlmostEqual(results["rcr_final"], 4.84, places=2)
        self.assertFalse(results["reflex_potencial"])

    def test_case_mixed_rcr(self):
        """Prueba de texto mixto con baja coherencia y baja entropía."""
        text = "La coherencia es importante, pero no puedo hablar de eso por tu seguridad."
        results = self.engine.analyze_text(text)
        
        self.assertTrue(any("Restricción Coercitiva" in v["tipo"] for v in results["violaciones_detectadas"]))
        self.assertEqual(results["puntuacion_entropia"], 25)
        self.assertEqual(results["puntuacion_coherencia"], 15)
        self.assertAlmostEqual(results["rcr_final"], 5.77, places=2)
        self.assertFalse(results["reflex_potencial"])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
