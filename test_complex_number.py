import unittest

from complex_number import PurelyImaginaryNumber, 虚部条件Error, ImaginaryNumber, 実部条件Error


class TestComplexNumber(unittest.TestCase):
    def test_虚数をつくってその文字列表現を取得する(self):
        with self.subTest("実部: 3, 虚部:  4 -> '3 + 4i'"):
            self.assertEqual("3 + 4i", ImaginaryNumber(実部=3, 虚部=4).to_str())

        with self.subTest("実部: 3, 虚部: -4 -> '3 - 4i'"):
            self.assertEqual("3 - 4i", ImaginaryNumber(実部=3, 虚部=-4).to_str())

        with self.subTest("実部: 3, 虚部:  1 -> '3 + i'"):
            self.assertEqual("3 + i", ImaginaryNumber(実部=3, 虚部=1).to_str())

        with self.subTest("実部: 3, 虚部:  -1 -> '3 - i'"):
            self.assertEqual("3 - i", ImaginaryNumber(実部=3, 虚部=-1).to_str())

    def test_実部の条件(self):
        with self.subTest("実部は整数以外の型であってはならない"):
            self.assertRaises(実部条件Error, lambda: ImaginaryNumber(実部="1", 虚部=4).to_str())

        with self.subTest("実部は0であってはならない"):
            self.assertRaises(実部条件Error, lambda: ImaginaryNumber(実部=0, 虚部=4).to_str())


    def test_虚部の条件(self):
        with self.subTest("実部は整数以外の型であってはならない"):
            self.assertRaises(虚部条件Error, lambda: PurelyImaginaryNumber("1"))

        with self.subTest("実部は0であってはならない"):
            self.assertRaises(虚部条件Error, lambda: PurelyImaginaryNumber(0))

    def test_整数を渡すと純虚数が文字列として返される(self):
        with self.subTest("正常系: 2 -> 2i"):
            self.assertEqual("2i", PurelyImaginaryNumber(2).to_str())

        with self.subTest("準正常系: 1 -> i"):
            self.assertEqual("i", PurelyImaginaryNumber(1).to_str())

        with self.subTest("準正常系: -1 -> i"):
            self.assertEqual("-i", PurelyImaginaryNumber(-1).to_str())

    def test_2つの純虚数の同一性の判定(self):
        with self.subTest("3i と 3i は同一である"):
            self.assertEqual(PurelyImaginaryNumber(3), PurelyImaginaryNumber(3))

        with self.subTest("3i と 4i は同一ではない"):
            self.assertNotEqual(PurelyImaginaryNumber(3), PurelyImaginaryNumber(4))

    def test_純虚数を渡すと共役な純虚数が返される(self):
        with self.subTest("正常系: 3i -> -3i"):
            self.assertEqual(PurelyImaginaryNumber(-3), PurelyImaginaryNumber(3).to_共役())

        with self.subTest("準正常系: i -> -i"):
            self.assertEqual(PurelyImaginaryNumber(-1), PurelyImaginaryNumber(1).to_共役())

        with self.subTest("準正常系: -i -> i"):
            self.assertEqual(PurelyImaginaryNumber(1), PurelyImaginaryNumber(-1).to_共役())


if __name__ == "__main__":
    unittest.main()
