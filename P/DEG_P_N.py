def DEG_P_N(P: Polynomial) -> Natural:
    """
    Сделал: Чумаков Никита Ярославович
    DEG_P_N: Polynomial → Natural
    Возвращает степень многочлена как натуральное число.
    """
    # Получаем степень многочлена (int)
    m = P.m

    # Преобразуем в массив цифр
    A = [int(d) for d in str(m)]

    # Создаём объект Natural
    N = Natural(len(A) - 1, A)

    return N