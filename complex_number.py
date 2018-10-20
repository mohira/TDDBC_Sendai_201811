class PurelyImaginaryNumber:
    def __init__(self, num: int=None):
        self.虚部 = num

    def create_純虚数_from整数(self, integer_number: int) -> str:
        if integer_number == 1:
            return "i"

        if integer_number == -1:
            return "-i"

        return "{}i".format(integer_number)

    def 同一ですか(self, 純虚数その1, 純虚数その2):
        return 純虚数その1 == 純虚数その2

    def create_共役な純虚数_from純虚数(self, 純虚数: str):
        虚部 = self.get_虚部(純虚数)

        return self.create_純虚数_from整数(-1 * 虚部)

    def get_虚部(self, 純虚数: str) -> int:
        if 純虚数 == "i":
            return 1

        if 純虚数 == "-i":
            return -1

        return int(純虚数[:-1])

    def value_as_str(self) -> str:
        if self.虚部 == 1:
            return "i"

        if self.虚部 == -1:
            return "-i"

        return f"{self.虚部}i"
