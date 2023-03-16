
import unittest

class TestExample(unittest.TestCase):

    def test_suma_numeros(self):
        n1 = 10
        n2 = 20

        resultado = n1 + n2
        self.assertEqual(resultado, 30)

    def test_resta_numeros(self):
        self.assertEqual(30 - 20, 10)

if __name__ == '__main__':
    unittest.main()
