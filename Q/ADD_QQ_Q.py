def ADD_QQ_Q(A: Rational, B: Rational) -> Rational:
    """
    Сделала: Имховик Наталья
    Выполняет сложение дробей
    Возвращает дробь
    """
    # Находим НОК знаменателей
    lcm = LCM_NN_N(A.denominator, B.denominator)

    # Находим дополнительные множители
    multiplyerA = lcm // A.denominator
    multiplyerB = lcm // B.denominator

    # Умножаем числители на дополнительные множители и складываем
    newNumerator = A.numerator * multiplyerA + B.numerator * multiplyerB

    # Создаем результирующую дробь
    return Rational(newNumerator, lcm)