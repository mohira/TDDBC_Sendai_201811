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

    def __eq__(self, other):
        return self.実部 == other.実部