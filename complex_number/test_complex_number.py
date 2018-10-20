import unittest


class ComplexNumber:
    def create_純虚数_from整数(self, integer_number: int) -> str:
        return f"{integer_number}i"


class TestImaginaryNumber(unittest.TestCase):
    def setUp(self):
        self.complex_number = ComplexNumber()

    def test_整数2を渡すと純虚数2iが文字列として返される(self):
        actual = self.complex_number.create_純虚数_from整数(integer_number=2)

        self.assertEqual("2i", actual)

    def test_整数3を渡すと純虚数3iが文字列として返される(self):
        actual = self.complex_number.create_純虚数_from整数(integer_number=3)

        self.assertEqual("3i", actual)

    def test_整数マイナス4を渡すと純虚数マイナス4iが文字列として返される(self):
        actual = self.complex_number.create_純虚数_from整数(integer_number=4)

        self.assertEqual("4i", actual)


if __name__ == "__main__":
    unittest.main()
