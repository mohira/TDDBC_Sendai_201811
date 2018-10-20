from complex_number.imaginary_unit import 虚数単位


class 虚部条件Error(Exception):
    # 数学の定義において虚部は実数だが、現状は0以外の整数のみを虚部の条件としている
    pass


class PurelyImaginaryNumber:
    def __init__(self, 虚部: int):
        if 虚部 == 0 or (not isinstance(虚部, int)):
            raise 虚部条件Error(f"{虚部}は0以外の整数である必要があります。")

        self.虚部 = 虚部

    def __eq__(self, other) -> bool:
        return self.虚部 == other.虚部

    def to_str(self) -> str:
        if self.虚部 == 1:
            return 虚数単位.plus.value

        if self.虚部 == -1:
            return 虚数単位.minus.value

        return f"{self.虚部}{虚数単位.plus.value}"

    def to_共役(self):
        return PurelyImaginaryNumber(-1 * self.虚部)


