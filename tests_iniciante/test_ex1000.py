from unittest import TestCase
from Ex1000 import mensagem


class Test_Hello_World(TestCase):
    def teste_hello(self):
        self.assertEquals(mensagem('Hello World!'), 'Hello World!')
