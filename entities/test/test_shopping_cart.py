import unittest
from entities.product import Product
from entities.shopping_cart import ShoppingCart
from entities.product import ProductDiscountError

def is_avaible_to_skip():
   return True

class TestShoppingCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Este método se ejecuta antes de TODAS las pruebas unitarias')

    @classmethod
    def tearDownClass(cls) -> None:
        print('Este método se ejecuta después de TODAS las pruebas unitarias')


    def setUp(self) -> None:
        print('El método setUp, se ejecuta antes de cada una de las pruebas.')
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShoppingCart()
        
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)


    def tearDown(self) -> None:
        print('El método tearDown, se ejecuta después de cada una de las pruebas.')


    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Lo sentimos, el carrito de compras no está vacío.')


    def test_shopping_cart_has_products(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())


    def test_products_in_shopping_cart(self):
        self.assertIn(self.smartphone, self.shopping_cart_2.products)


    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone)

        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)


    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name='Example', price=10.0, discount=11.0)


    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Libro', price=15.0))
        self.shopping_cart_1.add_product(Product(name='Cámara', price=700.0, discount=70))
        self.shopping_cart_1.add_product(Product(name='PC', price=1000, discount=0.0))

        self.assertGreater(self.shopping_cart_1.total, 0) # >
        self.assertLess(self.shopping_cart_1.total, 2000) # <

        self.assertEqual(self.shopping_cart_1.total, 1645.00)


    def test_total_emptty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0)


    @unittest.skip('La pruba noo cumple con los requerimientos necesarios.')
    def test_skip_example(self):
        self.assertEqual(1, 1)

    
    @unittest.skipIf(is_avaible_to_skip(), 'No se cuenta con todos los requerimientos.')
    def test_skip_example_two(self):
        pass

    #skipIf -> Evalua sobre Verdadero
    #skipUnless -> Evalua sobre falso

    def test_code_product(self):
        self.assertRegex(self.smartphone.code, 'busca este texto', 'Lo sentimos, no se eencuentra el código de prooducto.')

if __name__ == '__main__':
    unittest.main()