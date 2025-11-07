def ADD_QQ_Q(self, other):
    """
    Сделала: Имховик Наталья
    Выполняет сложение дробей
    Возвращает дробь
    """
    # Находим НОК знаменателей
    lcm = LCM_NN_N(self.denominator, other.denominator)

    # Находим дополнительные множители
    multiplyerA = lcm // self.denominator
    multiplyerB = lcm // other.denominator

    # Умножаем числители на дополнительные множители и складываем
    newNumerator = self.numerator * multiplyerA + other.numerator * multiplyerB

    # Создаем результирующую дробь
    return Rational(newNumerator, lcm)