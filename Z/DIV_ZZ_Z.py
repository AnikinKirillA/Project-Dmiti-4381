def __truediv__(self, other):
    """
    Сделал: Соколовский Артём
    Деление целых чисел: self / other (целая часть, округление к нулю).
    """

    # Проверка на ноль
    if all(d == 0 for d in other.A):
        raise ZeroDivisionError("Деление на ноль")

    # Определяем знак результата
    result_sign = 1 if self.s != other.s else 0

    # Берём модули чисел
    abs_self = ABS_Z_N(self)   
    abs_other = ABS_Z_N(other) 

    # Проверка, если |a| < |b| → результат = 0
    if COM_NN_D(abs_self, abs_other) == -1:
        return Integer(0, 0, [0])

    # Выполняем деление как для натуральных
    quotient_nat = DIV_NN_N(abs_self, abs_other)

    # Формируем результат
    return Integer(result_sign, quotient_nat.len, quotient_nat.A)

