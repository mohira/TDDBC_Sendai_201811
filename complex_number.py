from enum import Enum


class 虚数単位(Enum):
    plus = "i"
    minus = "-i"


class 虚部条件Error(Exception):
    # 数学の定義において虚部は実数だが、現状は0以外の整数のみを虚部の条件としている
    pass


class PurelyImaginaryNumber:
    def __init__(self, 虚部: int):
        if 虚部 == 0 or (not isinstance(虚部, int)):
            raise 虚部条件Error(f"{虚部}は0以外の整数である必要があります。")

        self.虚部 = 虚部

    def __eq__(self, other) -> bool:
        # 純虚数は実部がないので虚部のみの比較でOKのはず
        return self.虚部 == other.虚部

    def to_str(self) -> str:
        if self.虚部 == 1:
            return 虚数単位.plus.value

        if self.虚部 == -1:
            return 虚数単位.minus.value

        return f"{self.虚部}{虚数単位.plus.value}"

    def to_共役(self):
        return PurelyImaginaryNumber(-1 * self.虚部)


class 実部条件Error(Exception):
    # 数学の定義において実部は実数だが、現状は0以外の整数を虚部の条件としている
    pass


class RealNumber:
    def __init__(self, 実部: int):
        if 実部 == 0 or (not isinstance(実部, int)):
            raise 実部条件Error(f"{実部}は0以外の整数である必要があります。")

        self.実部 = 実部

    def to_str(self):
        return str(self.実部)


class ImaginaryNumber:
    def __init__(self, 実部: int, 虚部: int):
        self.実部 = RealNumber(実部)
        self.純虚数 = PurelyImaginaryNumber(虚部)

    def to_str(self) -> str:
        if self.純虚数.虚部 > 0:
            return f"{self.実部.to_str()} + {self.純虚数.to_str()}"

        if self.純虚数.虚部 < 0:
            return f"{self.実部.to_str()} - {self.純虚数.to_共役().to_str()}"
