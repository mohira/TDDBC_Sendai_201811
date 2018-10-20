from purely_imaginary_number import PurelyImaginaryNumber
from real_number import RealNumber


class ImaginaryNumber:
    def __init__(self, 実部: int, 虚部: int):
        self.実部 = RealNumber(実部)
        self.純虚数 = PurelyImaginaryNumber(虚部)

    def to_str(self) -> str:
        if self.純虚数.虚部 > 0:
            return f"{self.実部.to_str()} + {self.純虚数.to_str()}"

        if self.純虚数.虚部 < 0:
            return f"{self.実部.to_str()} - {self.純虚数.to_共役().to_str()}"
