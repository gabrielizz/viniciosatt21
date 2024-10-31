# Gabriel Gonçalves
# Fase Refactor

import unittest
from funcao_calculo import calcular_media_nota

class TestCalculadora(unittest.TestCase):
    
    # Teste básico com três notas comuns
    def test_media_basica(self):
        self.assertEqual(calcular_media_nota([40, 50, 60]), 50)

    # Teste com todas as notas zero
    def test_notas_zero(self):
        self.assertEqual(calcular_media_nota([0, 0, 0]), 0)
        
    # Teste com todas as notas no valor máximo (considerando 100 como máximo)
    def test_notas_maximas(self):
        self.assertEqual(calcular_media_nota([100, 100, 100]), 100)
        
    # Teste com notas que têm valores decimais
    def test_notas_decimais(self):
        self.assertAlmostEqual(calcular_media_nota([12.5, 28.3, 13.7]), 18.166666666666668)

    # Teste com uma combinação de valores máximos, zero e decimal
    def test_notas_misturadas(self):
        self.assertAlmostEqual(calcular_media_nota([0, 100, 50.8]), 50.27, places=2)

    # Teste com uma lista vazia
    def test_lista_vazia(self):
        self.assertIsNone(calcular_media_nota([]), "A média de uma lista vazia deve ser None.")

    # Teste com entrada inválida (não é uma lista)
    def test_entrada_invalida_tipo(self):
        with self.assertRaises(ValueError):
            calcular_media_nota("não é uma lista")

    # Teste com elementos não numéricos na lista
    def test_elementos_nao_numericos(self):
        with self.assertRaises(ValueError):
            calcular_media_nota([10, "vinte", 30])

if __name__ == '__main__':
    unittest.main()
