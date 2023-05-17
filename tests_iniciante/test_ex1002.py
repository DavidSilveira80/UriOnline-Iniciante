from exerciciosIniciante.Ex1002 import area, retorna_com_quatro_casas, retorna_saida
from unittest import TestCase


class TestEx1002(TestCase):

    def test_quatro_casas_decimais(self):
        self.assertEqual(retorna_com_quatro_casas(12.56636), '12.5664')

    def test_saida(self):
        self.assertEqual(retorna_saida('12.5664'), 'A=12.5664')
