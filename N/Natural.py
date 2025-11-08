class Natural:
    def __init__(self, n, A):
        self.A = A #[] массив из int   123 -> [1, 2, 3]
        self.len = n #int len(A)-1

    def TRANS_N_Z(self):
        """
        Сделала: Имховик Наталья
        Преобразование натурального в целое
        Возвращает целое
        """
        # Формируем положительное целое с полями натурального
        return Integer(0, self.len, self.A[:])

    def COM_NN_D(self, other):
        """
        Сделал: Соколовский Артём
        Сравнение двух натуральных чисел (self и other).

        Возвращает:
            1  — если self > other
            0  — если self == other
            -1 — если self < other
        """
        A = self.A[:]
        B = other.A[:]

        # Убираем ведущие нули
        while len(A) > 1 and A[0] == 0:
            A.pop(0)
        while len(B) > 1 and B[0] == 0:
            B.pop(0)

        # Сравнение по длине
        if len(A) > len(B):
            return 1
        elif len(A) < len(B):
            return -1

        # Поразрядное сравнение
        for da, db in zip(A, B):
            if da > db:
                return 1
            elif da < db:
                return -1

        return 0

    def NZER_N_B(self):
        """
        Богданов Никита Константинович
        Проверка на ноль натурального числа
        """
        # Число равно нулю, если оно состоит из одной цифры и эта цифра 0
        return self.len == 0 and self.A[0] == 0

    def ADD_1N_N(self):
        """
        Выполнил: Сурин Максим
        Добавление 1 к натуральному числу
        """

        rev_num = self.A.reverse()  # Запись числа справа налево
        rev_num[0] += 1  # Прибавление единицы к разряду единиц

        """ Перенос единиицы при переполнении разряда """
        for i in range(self.len + 1):
            if rev_num[i] == 10:
                rev_num[i] = 0
                if i < self.len:
                    rev_num[i + 1] += 1
                else:
                    rev_num.append(1)

        return Natural(len(rev_num) - 1, rev_num.reverse())

    def __add__(self, other):
        """
        Сделал: Соколовский Артём
        Сложение двух натуральных чисел: self + other.
        """
        A = self.A[::-1]
        B = other.A[::-1]
        res = []
        carry = 0

        for i in range(max(len(A), len(B))):
            da = A[i] if i < len(A) else 0
            db = B[i] if i < len(B) else 0
            s = da + db + carry
            res.append(s % 10)
            carry = s // 10

        if carry:
            res.append(carry)

        res.reverse()
        return Natural(len(res) - 1, res)

    def __sub__(self, other):
        """
        Сделал: Соколовский Артём
        Вычитание натуральных чисел: self - other (при self >= other).
        """
        if self.COM_NN_D(other) == -1:
            raise ValueError("SUB_NN_N: self < other")

        A = self.A[::-1]
        B = other.A[::-1]
        res = []
        borrow = 0

        for i in range(len(A)):
            da = A[i]
            db = B[i] if i < len(B) else 0
            diff = da - db - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            res.append(diff)

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        res.reverse()
        return Natural(len(res) - 1, res)

    def MUL_ND_N(self, int):
        """
        Выполнил: Сурин Максим
        Умножение натурального числа на цифру
        """

        rev_num = self.A.reverse()  # Запись числа справа налево

        """ Домножение каждого разряда на цифру """
        for i in range(self.len + 1):
            rev_num[i] *= int

        """ Перенос при переполнении разряда """
        for i in range(self.len + 1):
            if rev_num[i] > 9:
                """ 
                В текущем разряде сохраняем единицы,
                в следующий переносим десятки
                """
                rev_num[i] %= 10
                if i < self.len:
                    rev_num[i + 1] = rev_num[i] // 10
                else:
                    rev_num.append(rev_num[i] // 10)

        return Natural(len(rev_num) - 1, rev_num.reverse())

    def MUL_Nk_N(self, other):
        """
        Богданов Никита Константинович
        Умножение натурального числа на 10^k
        """

        # Если число 0 или k = 0, возвращаем исходное число
        if self.NZER_N_B() or other.NZER_N_B():
            return Natural(self.len, self.A[:])

        # Получаем значение k как целое число (количество нулей)
        k_value = 0
        multiplier = 1
        for i in range(other.len, -1, -1):
            k_value += other.A[i] * multiplier
            multiplier *= 10

        # Копируем существующие цифры со сдвигом на k позиций
        new_A = self.A + [0] * k_value

        new_len = len(new_A) - 1
        return Natural(new_len, new_A)

    def __mul__(self, other):
        """
        Богданов Никита Константинович
        Умножение натуральных чисел
        """
        if not isinstance(other, Natural):
            raise TypeError("The multipliers must be Natural")

        # Если одно из чисел равно нулю, возвращаем ноль
        if self.NZER_N_B() or other.NZER_N_B():
            return Natural(0, [0])

        # Инициализируем результат как 0
        result = Natural(0, [0])

        # Умножаем каждую цифру N2 на N1 и складываем со сдвигом
        for i in range(other.len, -1, -1):
            digit = other.A[i]

            temp_product = self.MUL_ND_N(digit)

            # Создаем сдвиг (умножение на 10^i), если i не самая младшая цифра
            if i < other.len:
                # Аналогия как умножение столбиком
                shift_value = other.len - i  # На сколько разрядов сдвигать
                shift_digits = [shift_value] if shift_value < 10 else [int(d) for d in str(shift_value)]
                shift_natural = Natural(len(shift_digits) - 1, shift_digits)

                # Сдвигаем
                shifted_product = temp_product.MUL_Nk_N(shift_natural)
            else:
                shifted_product = temp_product

            # Складываем с результатом
            result = result + shifted_product

        return result

    def SUB_NDN_N(self, int, other):
        """
        Выполнил: Сурин Максим
        Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом
        """

        other_num = other.MUL_ND_N(int)  # Домножение второго числа на цифру

        if self.COM_NN_D(other_num) == -1:  # При отрицательном результате возвращаем ноль
            return Natural(0, [0])

        return self - other_num

    def DIV_NN_Dk(self, other) -> (int, int):
        """
        Сделал: Захаренко Александр
        Вычисление первой цифры деления большего натурального
        на меньшее, домноженное на 10^k,
        где k - номер позиции этой цифры (номер считается с нуля)
        """

        # Проверяем, что self >= other
        if self.COM_NN_D(other) == -1:
            return 0, 0

        # Определяем позицию k
        k = self.len - other.len

        # Если после сдвига other становится больше self, уменьшаем k
        if k > 0:
            other_shifted = other.MUL_Nk_N(k)
            if self.COM_NN_D(other_shifted) == -1:
                k -= 1

        # Если k стал отрицательным, возвращаем 0
        if k < 0:
            return 0, 0

        # Ищем цифру от 9 до 1
        for digit in range(9, 0, -1):
            other_shifted = other.MUL_Nk_N(k)

            # Преобразуем в числа для проверки
            other_shifted_num = int("".join(map(str, other_shifted.A)))
            self_num = int("".join(map(str, self.A)))

            if digit * other_shifted_num <= self_num:
                return digit, k

        return 1, k

    def __floordiv__(self, other):
        """
        Сделал: Захаренко Александр
        Неполное частное от деления первого натурального числа
        на второе с остатком (делитель отличен от нуля)
        """

        # Проверка деления на ноль
        if all(x == 0 for x in other.A):
            raise ZeroDivisionError("Division by zero")

        # Если делимое меньше делителя, возвращаем 0
        if self.COM_NN_D(other) == -1:
            return Natural(1, [0])

        # Определяем максимальную длину результата
        max_length = self.len - other.len + 1
        result_digits = [0] * max_length  # массив для цифр результата

        current = Natural(self.len, self.A.copy())  # текущий остаток

        # Пока текущий остаток >= other
        while current.COM_NN_D(other) != -1:
            # Получаем очередную цифру и её позицию
            digit, k = current.DIV_NN_Dk(other)

            # Если цифра 0, значит деление завершено
            if digit == 0:
                break

            # Записываем цифру в результат на соответствующую позицию
            result_digits[k] = digit

            # Вычитаем: current = current - digit * other * 10^k
            other_shifted = other.MUL_Nk_N(k)  # other * 10^k
            current = current.SUB_NDN_N(other_shifted, digit)

            # Если остаток стал нулевым, завершаем
            if all(x == 0 for x in current.A):
                break

        # Убираем ведущие нули
        while len(result_digits) > 1 and result_digits[-1] == 0:
            result_digits.pop()

        # Разворачиваем массив (т.к. у нас старшие разряды в конце)
        result_digits.reverse()

        return Natural(len(result_digits), result_digits)

    # вместо MOD_NN_N (переопределяем Остаток от деления %)
    def __mod__(self, other):
        """
        Сделал: Захаренко Александр
        Остаток от деления первого натурального числа
        на второе натуральное (делитель отличен от нуля)
        """

        q = self // other  # Целая часть от деления self на other, Natural
        digit = int("".join(map(str, q.A)))  # Перевели Natural q в int digit, чтобы воспользоваться SUB_NDN_N

        return self.SUB_NDN_N(digit, other)  # self - other * digit

    def GCF_NN_N(self, other):
        """
        Сделал: Чумаков Никита Ярославович
        НОД (наибольший общий делитель) двух натуральных чисел.
        """
        # Создаём копии, чтобы не испортить исходные
        A = Natural(self.len, self.A[:])
        B = Natural(other.len, other.A[:])

        while B.NZER_N_B():  # пока B != 0
            # Проверяем, какое больше
            cmp = A.COM_NN_D(B)

            if cmp == 1:  # A < B -> поменяем их местами
                A, B = B, A

            # Теперь A >= B, можно брать остаток
            R = A % B
            A, B = B, R

        return A

    def LCM_NN_N(self, other):
        """
        Сделала: Имховик Наталья
        Нахождение НОК натуральных чисел
        Используем НОК(a, b) = (a * b) / НОД(a, b)
        Возвращает натуральное
        """
        gcd = self.GCF_NN_N(other)
        return self * other // gcd

