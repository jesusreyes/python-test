import unittest
from entities.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self) -> None:
        print('El método setUp, se ejecuta antes de cada una de las pruebas.')
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)

    def test_product_example(self):
        self.assertEqual(1, 1)


    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        product = Product(name, price)

        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price, 'Lo sentimos, el precio no es el mismo.')


    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)


    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)
