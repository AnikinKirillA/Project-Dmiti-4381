def MUL_Nk_N(N: Natural, k: Natural)-> Natural:
    """
    Богданов Никита Константинович
    Умножение натурального числа на 10^k
    """

    # Если число 0 или k = 0, возвращаем исходное число
    if NZER_N_B(N) or NZER_N_B(k):
        return Natural(N.len, N.A[:])

    # Получаем значение k как целое число (количество нулей)
    k_value = 0
    multiplier = 1
    for i in range(k.len, -1, -1):
        k_value += k.A[i] * multiplier
        multiplier *= 10

    # Копируем существующие цифры со сдвигом на k позиций
    new_A = N.A + [0] * k_value

    new_len = len(new_A) - 1
    return Natural(new_len, new_A)
