import unittest
import lab1_9

class TestLab_9(unittest.TestCase):
    def test_decimal2Roman(self):
        self.assertEqual(lab1_9.decimal2roman(1), "I")
        self.assertEqual(lab1_9.decimal2roman(15), "XV")
        self.assertEqual(lab1_9.decimal2roman(23), "XXIII")
        self.assertEqual(lab1_9.decimal2roman(545454), "D̅X̅L̅V̅CDLIV")
        self.assertEqual(lab1_9.decimal2roman(19999), "X̅MX̅CMXCIX")
        self.assertEqual(lab1_9.decimal2roman(252456), "C̅C̅L̅MMCDLVI")
        self.assertEqual(lab1_9.decimal2roman(3999999999), "M̿M̿M̿C̿M̿X̿C̿M̿X̿C̅M̅X̅C̅MX̅CMXCIX")

    def test_decimal2Roman_type(self):
        self.assertRaises(TypeError, lab1_9.decimal2roman, "hello")
        self.assertRaises(TypeError, lab1_9.decimal2roman, )
        self.assertRaises(TypeError, lab1_9.decimal2roman, True)

    def test_decimal2Roman_value(self):
        self.assertRaises(ValueError, lab1_9.decimal2roman, -1)
        self.assertRaises(ValueError, lab1_9.decimal2roman, 0)
        self.assertRaises(ValueError, lab1_9.decimal2roman, 40000000000)

