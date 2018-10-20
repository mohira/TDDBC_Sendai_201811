from complex_number.imaginary_unit import ImaginaryUnit


class ImaginaryPartConditionError(Exception):
    # 数学の定義では虚部は実数であることが条件だが、現状は0以外の整数のみを虚部条件とするのが仕様
    pass


class PurelyImaginaryNumber:
    def __init__(self, imaginary_part: int):
        if imaginary_part == 0 or (not isinstance(imaginary_part, int)):
            raise ImaginaryPartConditionError(f"{imaginary_part}は虚部条件を満たしません。虚部は0以外の整数である必要があります。")

        self.value = imaginary_part

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def notation(self) -> str:
        if self.value == 1:
            return ImaginaryUnit.plus.value

        if self.value == -1:
            return ImaginaryUnit.minus.value

        return f"{self.value}{ImaginaryUnit.plus.value}"

    def to_conjugate(self):
        return PurelyImaginaryNumber(-1 * self.value)
