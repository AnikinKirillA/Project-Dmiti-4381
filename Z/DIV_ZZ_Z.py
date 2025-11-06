def __truediv__(self, other):
    """
    Сделал: Соколовский Артём
    Деление целых чисел: self / other.
    """
    if all(d == 0 for d in other.A):
        raise ZeroDivisionError("DIV_ZZ_Z: деление на ноль")

    A = int(''.join(map(str, self.A))) if self.A else 0
    B = int(''.join(map(str, other.A))) if other.A else 0

    q_abs = abs(A) // abs(B)
    result_sign = 1 if self.s != other.s else 0

    if q_abs == 0:
        return Integer(0, 0, [0])

    digits = [int(ch) for ch in str(q_abs)]
    return Integer(result_sign, len(digits) - 1, digits)
