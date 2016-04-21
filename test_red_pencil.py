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

    def test_is_red_pencil__stable_price_5_discount_returns_true(self):
        prices = [100] * 30
        red_pencils = [False] * len(prices)
        prices.append(95)
        red_pencils.append(True)
        self.assertEquals(is_red_pencil(prices), red_pencils, "Stable prices followed by 5% drop should be true.")

    def test_is_red_pencil__stable_price_4_discount_returns_false(self):
        prices = [100] * 30
        red_pencils = [False] * len(prices)
        prices.append(96)
        red_pencils.append(False)
        self.assertEquals(is_red_pencil(prices), red_pencils, "Stable prices followed by 4% drop should be false.")

    def test_is_red_pencil__stable_price_31_discount_returns_false(self):
        prices = [100] * 30
        red_pencils = [False] * len(prices)
        prices.append(69)
        red_pencils.append(False)
        self.assertEquals(is_red_pencil(prices), red_pencils, "Stable prices followed by 31% drop should be false.")

    def test_is_red_pencil__stable_price_25_discount_returns_true_repeatedly_if_sale_continues(self):
        prices = [100] * 30
        red_pencils = [False] * len(prices)
        prices.extend([75] * 5)
        red_pencils.extend([True] * 5)
        self.assertEquals(is_red_pencil(prices), red_pencils, "Stable prices followed by 25% drop should be true.")

    def test_is_red_pencil__red_pencil_discount_stops_on_price_increase(self):
        prices = [100] * 30
        red_pencils = [False] * len(prices)
        prices.extend([75, 75, 75, 80])
        red_pencils.extend([True, True, True, False])
        self.assertEquals(is_red_pencil(prices), red_pencils, "Red pencil discount should stop when the price goes up.")

