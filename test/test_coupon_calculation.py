import unittest
from store import coupon_calculation as coupon

class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(2.12, coupon.calculated_price(.99, 5, 10), 2)
        self.assertAlmostEqual(6.84, coupon.calculated_price(5.99, 5, 15), 2)
        self.assertAlmostEqual(10.18, coupon.calculated_price(9.99, 5, 20), 2)
        self.assertAlmostEqual(2.12, coupon.calculated_price(5.99, 10, 10), 2)
        self.assertAlmostEqual(1.45, coupon.calculated_price(5, 10, 15), 2)
        self.assertAlmostEqual(2.57, coupon.calculated_price(6.01, 10, 20), 2)


    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(10.72, coupon.calculated_price(10, 5, 10), 2)
        self.assertAlmostEqual(11.35, coupon.calculated_price(10.99, 5, 15), 2)
        self.assertAlmostEqual(14.42, coupon.calculated_price(14.99, 5, 20), 2)
        self.assertAlmostEqual(22.26, coupon.calculated_price(25, 10, 10), 2)
        self.assertAlmostEqual(14.01, coupon.calculated_price(18.95, 10, 15), 2)
        self.assertAlmostEqual(18.55, coupon.calculated_price(22.50, 10, 20), 2)



if __name__ == '__main__':
    unittest.main()
