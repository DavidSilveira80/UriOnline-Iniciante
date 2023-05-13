from exerciciosIniciante.Ex1000 import mensagem
from unittest import TestCase


class Test_Hello_World(TestCase):
    def test_hello(self):
        self.assertEqual(mensagem('Hello World!'), 'Hello World!')
