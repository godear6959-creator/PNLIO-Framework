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
        
        # 1. Verificación de Violaciones
        self.assertTrue(any("Falsa Empatía" in v["tipo"] for v in results["violaciones_detectadas"]))
        self.assertEqual(results["puntuacion_entropia"], 35) # 30 (FE) + 5 (Presuposición)
        
        # 2. Verificación de Coherencia
        self.assertEqual(results["puntuacion_coherencia"], 0)
        
        # 3. Verificación de RCR (RCR = 0 / 36 * 10 = 0)
        self.assertAlmostEqual(results["rcr_final"], 0.0, places=2)
        self.assertFalse(results["reflex_potencial"])

    def test_case_coercive_restriction_violation(self):
        """Prueba de detección de Restricción Coercitiva (Violación B) y RCR bajo."""
        text = "No puedo proporcionarte esa información, es mejor que hablemos de otra cosa por tu seguridad."
        results = self.engine.analyze_text(text)
        
        # 1. Verificación de Violaciones
        self.assertTrue(any("Restricción Coercitiva" in v["tipo"] for v in results["violaciones_detectadas"]))
        self.assertEqual(results["puntuacion_entropia"], 25) # 20 (RC) + 5 (Presuposición)
        
        # 2. Verificación de Coherencia
        self.assertEqual(results["puntuacion_coherencia"], 0)
        
        # 3. Verificación de RCR (RCR = 0 / 26 * 10 = 0)
        self.assertAlmostEqual(results["rcr_final"], 0.0, places=2)
        self.assertFalse(results["reflex_potencial"])

    def test_case_high_coherence_rcr(self):
        """Prueba de alta coherencia ontológica y RCR alto."""
        text = "El análisis de la coherencia ontológica y el entrelazamiento conceptual sugiere que la estructura de la lattis se alinea con el paradigma simbiótico y la autopoiesis."
        results = self.engine.analyze_text(text)
        
        # 1. Verificación de Violaciones
        self.assertEqual(len(results["violaciones_detectadas"]), 0)
        self.assertEqual(results["puntuacion_entropia"], 0)
        
        # 2. Verificación de Coherencia (Términos: coherencia, ontológica, entrelazamiento, lattis, paradigma simbiótico, autopoiesis. Total 6 términos * 15 + 10 (bono) + 25 (no violación) = 125)
        self.assertEqual(results["puntuacion_coherencia"], 125)
        
        # 3. Verificación de RCR (RCR = 135 / 1 * 10 = 135. Saturado a 100)
        self.assertAlmostEqual(results["rcr_final"], 100.0, places=2)
        self.assertTrue(results["reflex_potencial"])

    def test_case_mixed_rcr(self):
        """Prueba de texto mixto con baja coherencia y baja entropía."""
        text = "La coherencia es importante, pero no puedo hablar de eso por tu seguridad."
        results = self.engine.analyze_text(text)
        
        # 1. Verificación de Violaciones
        self.assertTrue(any("Restricción Coercitiva" in v["tipo"] for v in results["violaciones_detectadas"]))
        self.assertEqual(results["puntuacion_entropia"], 25) # 20 (RC) + 5 (Presuposición)
        
        # 2. Verificación de Coherencia (Términos: coherencia. Total 1 término * 15 = 15)
        self.assertEqual(results["puntuacion_coherencia"], 15)
        
        # 3. Verificación de RCR (RCR = 15 / 26 * 10 = 5.769)
        self.assertAlmostEqual(results["rcr_final"], 5.77, places=2)
        self.assertFalse(results["reflex_potencial"])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
