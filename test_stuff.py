import unittest
from vending_machine import give_change


class TestVendingMachine(unittest.TestCase):
    def test_this_thing_is_on(self):
        self.assertEquals(1, 1)

    def give_change(self, amount):
        return [10, 5, 2]

    def test_return_change(self):
        self.assertEqual(give_change(17), [10, 5, 2], 'wrong change given')
        self.assertEqual(give_change(18), [10, 5, 2, 1], 'wrong change given')

    def test_multiple_same_coins(self):
        self.assertEqual(give_change(4), [2, 2])

    def test_return_change(self):
        self.assertEqual(give_change(.17), [.10, .05, .02])
        self.assertEqual(give_change(.18), [.10, .05, .02, 01])
        self.assertEqual(give_change(.04), [.02, .02])

