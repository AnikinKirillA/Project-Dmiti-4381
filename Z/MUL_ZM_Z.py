def MUL_ZM_Z(self):
    """
    Сделал: Захаренко Александр
    Умножение целого на (-1)
    """
    new_s = 0 if self.s == 1 else 1             # меняем знак числа
    return Integer(new_s, self.len, self.A)     # формируем новое целое число с поменянным знаком