class ComplexNumber:
    def create_純虚数_from整数(self, integer_number: int) -> str:
        if integer_number == 1:
            return "i"

        if integer_number == -1:
            return "-i"

        return f"{integer_number}i"

    def 同一ですか(self, 純虚数その1, 純虚数その2):
        return 純虚数その1 == 純虚数その2
