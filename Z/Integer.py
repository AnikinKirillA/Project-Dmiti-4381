from N.Natural import Natural
from TRANS.TRANS_N_Z import TRANS_N_Z
from TRANS.TRANS_Z_N import TRANS_Z_N

class Integer:
    def __init__(self, s, n, A):
        self.s = s #int знак числа (1 — минус, 0 — плюс)
        self.len = n #int len(A)-1
        self.A = A #[] массив из int   123 -> [1, 2, 3], -123 -> [1, 2, 3]

    def ABS_Z_Z(self):
        """
        Сделала: Имховик Наталья
        Определение абсолютной величины числа
        Возвращает целое
        """
        # Устанавливаем знак +
        self.s = 0
        return self

    def SGN_Z_D(self):
        """
        Сделал: Чумаков Никита Ярославович
        Определение знака целого числа:
        -1 — положительное
         0 — равно нулю
         1 — отрицательное
        """
        # Проверим, что число не ноль
        if all(d == 0 for d in self.A):  # Если массив нулей -> z = 0
            return 0
        # Если знак отрицательный (s == 1)
        elif self.s == 1:
            return 1
        # Иначе положительное
        else:
            return -1

    def MUL_ZM_Z(self):
        """
        Сделал: Захаренко Александр
        Умножение целого на (-1)
        """

        # Проверям, не пытаемся ли заменить знак у нуля
        if self.A == [0]: return self  # для нуля возвращаем его же, не меняя знак

        # Иначе, число не ноль
        new_s = 0 if self.s == 1 else 1  # меняем знак числа
        return Integer(new_s, self.len, self.A)  # формируем новое целое число с противоположным знаком

    def __sub__(self, other):
        """
        Выполнил: Сурин Максим
        Вычитание целых чисел
        """

        """ Если первое число - ноль, возвращаем второе с противоположным знаком """
        if self.SGN_Z_D() == 0:
            return other.MUL_ZM_Z()

        """ Если второе число - ноль, возвращаем первое """
        if other.SGN_Z_D() == 0:
            return self

        """ 
        Если числа одного знака - вычитаем из большего меньшее;
        если большее - вычитаемое, знак минус, иначе плюс
        """
        if self.SGN_Z_D() == other.SGN_Z_D():
            n1 = Natural(self.len, self.A)
            n2 = Natural(other.len, other.A)

            if n1.COM_NN_D(n2) != -1:
                sub_of_mods = n1 - n2
                if self.SGN_Z_D == -1:
                    sign = 1
                else:
                    sign = 0

                return Integer(sign, sub_of_mods.len, sub_of_mods.A)
            else:
                sub_of_mods = n1 - n2
                if self.SGN_Z_D == -1:
                    sign = 0
                else:
                    sign = 1

                return Integer(sign, sub_of_mods.len, sub_of_mods.A)

        """ Если числа разных знаков - складываем модули и устанавливаем общий знак """
        if self.SGN_Z_D() != other.SGN_Z_D():
            sum_of_mods = Natural(self.len, self.ABS_Z_Z().A) + Natural(other.len, other.ABS_Z_Z().A)
            return Integer(self.s, sum_of_mods.len, sum_of_mods.A)

    def __mul__(self, other):
        """
        Сделал: Соколовский Артём
        Умножение целых чисел: self * other.
        """
        sign = 1 if self.s != other.s else 0  # знак результата

        A = self.A[::-1]
        B = other.A[::-1]
        res = [0] * (len(A) + len(B))

        for i in range(len(A)):
            carry = 0
            for j in range(len(B)):
                prod = res[i + j] + A[i] * B[j] + carry
                res[i + j] = prod % 10
                carry = prod // 10
            if carry:
                res[i + len(B)] += carry

        # убираем ведущие нули
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        res.reverse()
        return Integer(sign, len(res) - 1, res)

    def __truediv__(self, other):
        """
        Сделал: Соколовский Артём
        Деление целых чисел (self / other).
        """

        # Проверка делителя на ноль
        if all(d == 0 for d in other.A):
            raise ZeroDivisionError("Деление на ноль в целых числах")

        # Определяем знак результата
        result_sign = 1 if self.s != other.s else 0

        # Берём модули чисел (натуральные части)
        abs_self = self.ABS_Z_N()
        abs_other = other.ABS_Z_N()

        # Если |self| < |other| → результат = 0
        if abs_self.COM_NN_D(abs_other) == -1:
            return Integer(0, 0, [0])

        # Используем целочисленное деление (без остатка)
        quotient = abs_self // abs_other  # базовый оператор для натуральных чисел

        # Формируем результат
        result = Integer(result_sign, quotient.len, quotient.A)

        return result

    def __mod__(self, other):
        """
        Богданов Никита Константинович
        Остаток от деления целого числа self на целое число other
        """
        # Проверяем что делитель не ноль
        if other.A == [0] and other.len == 0:
            raise ValueError('You cant divide by zero.')

        # Вычисляем частное
        quotient = self // other

        # Вычисляем произведение делителя и частного
        product = other * quotient

        # Вычисляем остаток
        remainder = self - product

        return remainder


