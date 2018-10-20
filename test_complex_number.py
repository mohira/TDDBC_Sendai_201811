import unittest

from complex_number import PurelyImaginaryNumber


class TestComplexNumber(unittest.TestCase):
    def setUp(self):
        self.complex_number = PurelyImaginaryNumber()

    def test_整数を渡すと純虚数が文字列として返される(self):
        with self.subTest("正常系: 2 -> 2i"):
            self.assertEqual("2i", PurelyImaginaryNumber(2).value_as_str())

        with self.subTest("準正常系: 1 -> i"):
            self.assertEqual("i", PurelyImaginaryNumber(1).value_as_str())

        with self.subTest("準正常系: -1 -> i"):
            self.assertEqual("-i", PurelyImaginaryNumber(-1).value_as_str())

    def test_2つの純虚数の同一性の判定(self):
        with self.subTest("3i と 3i は同一である"):
            self.assertEqual(PurelyImaginaryNumber(3), PurelyImaginaryNumber(3))

        with self.subTest("3i と 4i は同一ではない"):
            self.assertNotEqual(PurelyImaginaryNumber(3), PurelyImaginaryNumber(4))

    def test_純虚数を渡すと共役な純虚数が返される(self):
        with self.subTest("正常系: 3i -> -3i"):
            純虚数3i = self.complex_number.create_純虚数_from整数(integer_number=3)
            self.assertEqual("-3i", self.complex_number.create_共役な純虚数_from純虚数(純虚数3i))

        with self.subTest("準正常系: i -> -i"):
            純虚数i = self.complex_number.create_純虚数_from整数(integer_number=1)

            self.assertEqual("-i", self.complex_number.create_共役な純虚数_from純虚数(純虚数i))

        with self.subTest("準正常系: -i -> i"):
            純虚数マイナスi = self.complex_number.create_純虚数_from整数(integer_number=-1)

            self.assertEqual("i", self.complex_number.create_共役な純虚数_from純虚数(純虚数マイナスi))


if __name__ == "__main__":
    unittest.main()
