from purely_imaginary_number import PurelyImaginaryNumber
from real_number import RealNumber


class ImaginaryNumber:
    def __init__(self, 実部: int, 虚部: int):
        self.実部 = RealNumber(実部)
        self.虚部 = PurelyImaginaryNumber(虚部)

    def __eq__(self, other):
        return (self.実部 == other.実部) and (self.虚部 == other.虚部)

    def to_str(self) -> str:
        if self.虚部.虚部 > 0:
            return f"{self.実部.to_str()} + {self.虚部.to_str()}"

        if self.虚部.虚部 < 0:
            return f"{self.実部.to_str()} - {self.虚部.to_共役().to_str()}"

    def to_共役(self):
        return ImaginaryNumber(self.実部.実部, self.虚部.to_共役().虚部)
