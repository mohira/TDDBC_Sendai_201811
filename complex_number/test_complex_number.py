import unittest

from complex_number.imaginary_number import ImaginaryNumber
from complex_number.purely_imaginary_number import PurelyImaginaryNumber, ImaginaryPartConditionError
from complex_number.real_number import RealPartConditionError


class TestComplexNumber(unittest.TestCase):
    def test_虚部の条件(self):
        with self.subTest("実部は整数以外の型であってはならない"):
            self.assertRaises(ImaginaryPartConditionError, lambda: PurelyImaginaryNumber("1"))

        with self.subTest("実部は0であってはならない"):
            self.assertRaises(ImaginaryPartConditionError, lambda: PurelyImaginaryNumber(0))

    def test_純虚数の生成とその文字列表現(self):
        with self.subTest("正常系: 2 -> '2i'"):
            self.assertEqual("2i", PurelyImaginaryNumber(2).notation())

        with self.subTest("準正常系: 1 -> 'i'"):
            self.assertEqual("i", PurelyImaginaryNumber(1).notation())

        with self.subTest("準正常系: -1 -> '-i'"):
            self.assertEqual("-i", PurelyImaginaryNumber(-1).notation())

    def test_2つの純虚数の同一性の判定(self):
        with self.subTest("3i と 3i は同一である"):
            self.assertEqual(PurelyImaginaryNumber(3), PurelyImaginaryNumber(3))

        with self.subTest("3i と 4i は同一ではない"):
            self.assertNotEqual(PurelyImaginaryNumber(3), PurelyImaginaryNumber(4))

    def test_共役な純虚数(self):
        with self.subTest("正常系: 3i と共役な純虚数は -3i"):
            self.assertEqual(PurelyImaginaryNumber(-3), PurelyImaginaryNumber(3).to_conjugate())

        with self.subTest("準正常系: i と共役な純虚数は -i"):
            self.assertEqual(PurelyImaginaryNumber(-1), PurelyImaginaryNumber(1).to_conjugate())

        with self.subTest("準正常系: -i と共役な純虚数は i"):
            self.assertEqual(PurelyImaginaryNumber(1), PurelyImaginaryNumber(-1).to_conjugate())

    def test_実部の条件(self):
        with self.subTest("実部は整数以外の型であってはならない"):
            self.assertRaises(RealPartConditionError, lambda: ImaginaryNumber("1", 4))

        with self.subTest("実部は0であってはならない"):
            self.assertRaises(RealPartConditionError, lambda: ImaginaryNumber(0, 4))

    def test_虚数の生成とその文字列表現(self):
        with self.subTest("実部: 3, 虚部:  4 -> '3 + 4i'"):
            self.assertEqual("3 + 4i", ImaginaryNumber(3, 4).notation())

        with self.subTest("実部: 3, 虚部: -4 -> '3 - 4i'"):
            self.assertEqual("3 - 4i", ImaginaryNumber(3, -4).notation())

        with self.subTest("実部: 3, 虚部:  1 -> '3 + i'"):
            self.assertEqual("3 + i", ImaginaryNumber(3, 1).notation())

        with self.subTest("実部: 3, 虚部:  -1 -> '3 - i'"):
            self.assertEqual("3 - i", ImaginaryNumber(3, -1).notation())

    def test_2つの虚数の同一性の判定(self):
        with self.subTest("「3 + 4i」と 「3 + 4i」 は同一である"):
            self.assertEqual(ImaginaryNumber(3, 4), ImaginaryNumber(3, 4))

        with self.subTest("「3 + 4i」と 「3 - 4i」 は同一ではない"):
            self.assertNotEqual(ImaginaryNumber(3, 4), ImaginaryNumber(3, -4))

    def test_共役な虚数(self):
        with self.subTest("「3 + 4i」の共役な複素数は「3 - 4i」"):
            self.assertEqual(ImaginaryNumber(3, -4), ImaginaryNumber(3, 4).to_conjugate())

        with self.subTest("「3 - 4i」の共役な複素数は「3 + 4i」"):
            self.assertEqual(ImaginaryNumber(3, 4), ImaginaryNumber(3, -4).to_conjugate())


if __name__ == "__main__":
    unittest.main()
