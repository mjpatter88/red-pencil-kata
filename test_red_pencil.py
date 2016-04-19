import unittest
from red_pencil import is_red_pencil

class TestRedPencil(unittest.TestCase):

    def test_is_red_pencil__price_not_stable_returns_false(self):
        prices = [100, 100, 100, 85]
        red_pencils = [False] * len(prices)
        self.assertEquals(is_red_pencil(prices), red_pencils, "Only four days of prices should always be false.")

    def test_is_red_pencil__stable_price_25_discount_returns_true(self):
        prices = [100] * 30
        red_pencils = [False] * len(prices)
        prices.append(75)
        red_pencils.append(True)
        self.assertEquals(is_red_pencil(prices), red_pencils, "Stable prices followed by 25% drop should be true.")
