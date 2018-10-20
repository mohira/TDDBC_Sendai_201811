from __future__ import annotations


class RealPartConditionError(Exception):
    # 数学の定義では実部は実数であることが条件だが、現状は0以外の整数のみを実部条件とするのが仕様
    pass


class RealNumber:
    def __init__(self, real_part: int):
        if real_part == 0 or (not isinstance(real_part, int)):
            raise RealPartConditionError(f"{real_part}は実部条件を満たしません。実部は0以外の整数である必要があります。")

        self.value = real_part

    def __eq__(self, other: RealNumber) -> bool:
        return self.value == other.value
