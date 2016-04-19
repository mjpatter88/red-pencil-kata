import unittest
from red_pencil import is_red_pencil

class TestRedPencil(unittest.TestCase):

    def test_is_red_pencil__price_not_stable_returns_false(self):
        prices = [100, 100, 100, 85]
        self.assertEquals(is_red_pencil(prices), False, "Only four days of prices should always be false.")
