import unittest
from discounts import apply_promo_code

class TestDiscounts(unittest.TestCase):
    def test_percentage_discount(self):
        self.assertEqual(apply_promo_code(10000, "SALE10"), 9000)

    def test_fixed_discount(self):
        self.assertEqual(apply_promo_code(10000, "WELCOME5000"), 5000)

    def test_invalid_promo(self):
        self.assertEqual(apply_promo_code(10000, "INVALID"), 10000)

if __name__ == "__main__":
    unittest.main()