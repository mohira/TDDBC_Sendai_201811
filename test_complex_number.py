import unittest

from complex_number import ComplexNumber


class TestComplexNumber(unittest.TestCase):
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

    def test_2つの純虚数の同一性の判定_同一である(self):
        純虚数その1 = self.complex_number.create_純虚数_from整数(integer_number=3)
        純虚数その2 = self.complex_number.create_純虚数_from整数(integer_number=3)

        self.assertTrue(self.complex_number.同一ですか(純虚数その1, 純虚数その2))

    def test_2つの純虚数の同一性の判定_同一でない(self):
        純虚数その1 = self.complex_number.create_純虚数_from整数(integer_number=3)
        純虚数その2 = self.complex_number.create_純虚数_from整数(integer_number=4)

        self.assertFalse(self.complex_number.同一ですか(純虚数その1, 純虚数その2))

    def test_純虚数を渡すと共役な純虚数が返される_正常系(self):
        純虚数3i = self.complex_number.create_純虚数_from整数(integer_number=3)

        self.assertEqual("-3i", self.complex_number.create_共役な純虚数_from純虚数(純虚数3i))

    def test_純虚数を渡すと共役な純虚数が返される_準正常系_その1(self):
        純虚数i = self.complex_number.create_純虚数_from整数(integer_number=1)

        self.assertEqual("-i", self.complex_number.create_共役な純虚数_from純虚数(純虚数i))

    def test_純虚数を渡すと共役な純虚数が返される_準正常系_その2(self):
        純虚数マイナスi = self.complex_number.create_純虚数_from整数(integer_number=-1)

        self.assertEqual("i", self.complex_number.create_共役な純虚数_from純虚数(純虚数マイナスi))


if __name__ == "__main__":
    unittest.main()
