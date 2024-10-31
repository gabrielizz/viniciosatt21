#Gabriel Gonçalves
#Fase Red

import unittest
from funcao_calculo import calcular_media_nota

class TestCalculadora(unittest.TestCase):
    
    # Teste básico com três notas comuns
    def test_media_basica(self):
        self.assertEqual(calcular_media_nota([40, 50, 60]), 20)

    # Teste com todas as notas zero  
    def test_notas_zero(self):
        self.assertEqual(calcular_media_nota([0, 0, 0]), 0)
        
    # Teste com todas as notas no valor máximo (considerando 100 como máximo)
    def test_notas_maximas(self):
        self.assertEqual(calcular_media_nota([100, 100, 100]), 100)
        
    # Teste com notas que têm valores decimais
    def test_notas_decimais(self):
        
        self.assertAlmostEqual(calcular_media_nota([12.5, 28.3, 13.7]), 22.5)

    # Teste com uma combinação de valores máximos, zero e decimal  
    def test_notas_misturadas(self):
        self.assertAlmostEqual(calcular_media_nota([0, 100, 50.8]), 50.17, places=2)

if __name__ == '__main__':
    unittest.main()
