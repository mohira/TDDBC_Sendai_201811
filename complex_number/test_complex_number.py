import unittest


class ComplexNumber:
    def create_純虚数_from整数(self, integer_number: int) -> str:
        return "2i"


class TestImaginaryNumber(unittest.TestCase):
    def test_整数2を渡すと純虚数2iが文字列として返される(self):
        complex_number = ComplexNumber()

        actual = complex_number.create_純虚数_from整数(integer_number=2)

        self.assertEqual("2i", actual)


if __name__ == "__main__":
    unittest.main()
