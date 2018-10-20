import unittest

from complex_number import ComplexNumber


class TestImaginaryNumber(unittest.TestCase):
    def setUp(self):
        self.complex_number = ComplexNumber()

    def test_整数を渡すと純虚数が文字列として返される_正常系(self):
        actual = self.complex_number.create_純虚数_from整数(integer_number=2)

        self.assertEqual("2i", actual)

    def test_整数を渡すと純虚数が文字列として返される_準正常系_その1(self):
        actual = self.complex_number.create_純虚数_from整数(integer_number=1)

        self.assertEqual("i", actual)

    def test_整数を渡すと純虚数が文字列として返される_準正常系_その2(self):
        actual = self.complex_number.create_純虚数_from整数(integer_number=-1)

        self.assertEqual("-i", actual)


if __name__ == "__main__":
    unittest.main()
