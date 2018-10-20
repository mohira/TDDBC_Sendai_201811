from enum import Enum


class 虚数単位(Enum):
    plus = "i"
    minus = "-i"


class PurelyImaginaryNumber:
    def __init__(self, num: int = None):
        self.虚部 = num

    def __eq__(self, other) -> bool:
        # 純虚数は実部がないので虚部のみの比較でOKのはず
        return self.虚部 == other.虚部

    def value_as_str(self) -> str:
        if self.虚部 == 1:
            return 虚数単位.plus.value

        if self.虚部 == -1:
            return 虚数単位.minus.value

        return f"{self.虚部}{虚数単位.plus.value}"

    def to_共役(self):
        return PurelyImaginaryNumber(-1 * self.虚部)
