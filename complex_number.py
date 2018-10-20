class ComplexNumber:
    def create_純虚数_from整数(self, integer_number: int) -> str:
        if integer_number == 1:
            return "i"

        if integer_number == -1:
            return "-i"

        return "{}i".format(integer_number)

    def 同一ですか(self, 純虚数その1, 純虚数その2):
        return 純虚数その1 == 純虚数その2

    def create_共役な純虚数_from純虚数(self, 純虚数: str):
        if 純虚数 == "i":
            return "-i"
        if 純虚数 == "-i":
            return "i"

        虚部 = int(純虚数[:-1])

        return "{}i".format(-1 * 虚部)
