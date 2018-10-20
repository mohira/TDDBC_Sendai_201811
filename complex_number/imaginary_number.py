from __future__ import annotations

from complex_number.purely_imaginary_number import PurelyImaginaryNumber
from complex_number.real_number import RealNumber


class ImaginaryNumber:
    def __init__(self, real_part: int, imaginary_part: int):
        self.real_part = RealNumber(real_part)
        self.imaginary_part = PurelyImaginaryNumber(imaginary_part)

    def __eq__(self, other: ImaginaryNumber) -> bool:
        return (self.real_part == other.real_part) and (self.imaginary_part == other.imaginary_part)

    def notation(self) -> str:
        if self.imaginary_part.value > 0:
            return f"{self.real_part.value} + {self.imaginary_part.notation()}"

        if self.imaginary_part.value < 0:
            return f"{self.real_part.value} - {self.imaginary_part.to_conjugate().notation()}"

    def to_conjugate(self) -> ImaginaryNumber:
        return ImaginaryNumber(self.real_part.value, self.imaginary_part.to_conjugate().value)
