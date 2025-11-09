from N.Natural import Natural
from Z.Integer import Integer
from TRANS.TRANS_N_Z import TRANS_N_Z


class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator  # Integer числитель
        self.denominator = denominator  # Natural знаменатель

    def RED_Q_Q(self):
        """
        Выполнил: Сурин Максим
        Сокращение дроби
        """
        # Если числитель равен нулю, возвращаем 0/1
        if self.numerator.A == [0]:
            return Rational(Integer(0, 0, [0]), Natural(0, [1]))

        # Получаем абсолютное значение числителя как натуральное число
        abs_numerator = self.numerator.ABS_Z_Z()
        numerator_natural = Natural(abs_numerator.len, abs_numerator.A)

        # Вычисляем НОД числителя и знаменателя
        gcf = numerator_natural.GCF_NN_N(self.denominator)

        # Создаем новый числитель и знаменатель
        new_numerator = self.numerator
        new_denominator = self.denominator

        # Если НОД не равен 1, сокращаем
        if gcf.A != [1]:
            # Делим числитель и знаменатель на НОД
            # Для числителя: преобразуем НОД в целое число и используем целочисленное деление
            new_numerator_abs = numerator_natural // gcf
            new_numerator = Integer(self.numerator.s, new_numerator_abs.len, new_numerator_abs.A)

            # Делим знаменатель на НОД
            new_denominator = self.denominator // gcf

        return Rational(new_numerator, new_denominator)

    def INT_Q_B(self) -> bool:
        """
        Сделал: Захаренко Александр
        Проверка сокращенного дробного на целое,
        если рациональное число является целым,
        то «да», иначе «нет»
        """
        # Сокращаем дробь и проверяем, равен ли знаменатель 1
        reduced = self.RED_Q_Q()
        return reduced.denominator.A == [1]

    def ADD_QQ_Q(self, other):
        """
        Сделала: Имховик Наталья
        Выполняет сложение дробей
        Возвращает дробь
        """
        # Находим НОК знаменателей
        lcm = self.denominator.LCM_NN_N(other.denominator)

        # Находим дополнительные множители используя целочисленное деление
        multiplierA = lcm // self.denominator
        multiplierB = lcm // other.denominator

        # Преобразуем натуральные множители в целые числа
        multiplierA_int = Integer(0, multiplierA.len, multiplierA.A)
        multiplierB_int = Integer(0, multiplierB.len, multiplierB.A)

        # Умножаем числители на дополнительные множители и складываем
        new_numerator = (self.numerator * multiplierA_int) + (other.numerator * multiplierB_int)

        # Создаем результирующую дробь
        return Rational(new_numerator, lcm).RED_Q_Q()

    def SUB_QQ_Q(self, other):
        """
        Сделала: Имховик Наталья
        Находит разность дробей
        Возвращает дробь
        """
        # Находим НОК знаменателей
        lcm = self.denominator.LCM_NN_N(other.denominator)

        # Находим дополнительные множители используя целочисленное деление
        multiplierA = lcm // self.denominator
        multiplierB = lcm // other.denominator

        # Преобразуем натуральные множители в целые числа
        multiplierA_int = Integer(0, multiplierA.len, multiplierA.A)
        multiplierB_int = Integer(0, multiplierB.len, multiplierB.A)

        # Умножаем числители на дополнительные множители и вычитаем
        new_numerator = (self.numerator * multiplierA_int) - (other.numerator * multiplierB_int)

        # Создаем результирующую дробь
        return Rational(new_numerator, lcm).RED_Q_Q()

    def __mul__(self, other):
        """
        Сделал: Чумаков Никита Ярославович
        Умножение двух рациональных чисел.
        Результат — новый Rational.
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        # Формируем новую дробь
        result = Rational(new_numerator, new_denominator)

        return result.RED_Q_Q()

    def __truediv__(self, other):
        """
        Сделал: Чумаков Никита Ярославович
        Деление рациональных чисел q1 / q2.
        Делитель q2 ≠ 0.
        Возвращает новый Rational.
        """
        # Проверим, что делитель не равен нулю
        if other.numerator.A == [0]:
            raise ZeroDivisionError("Деление на ноль в рациональных числах")

        # По формуле: (a/b) ÷ (c/d) = (a*d) / (b*c)
        # Преобразуем знаменатель other в целое число
        other_denominator_int = TRANS_N_Z(other.denominator)

        # Получаем абсолютное значение числителя other
        other_numerator_abs = other.numerator.ABS_Z_Z()

        # Умножаем
        new_numerator = self.numerator * other_denominator_int
        new_denominator = self.denominator * Natural(other_numerator_abs.len, other_numerator_abs.A)

        # Учитываем знак
        if other.numerator.s == 1:  # Если other отрицательный, меняем знак
            new_numerator = new_numerator.MUL_ZM_Z()

        # Формируем новое рациональное число
        result = Rational(new_numerator, new_denominator)

        return result.RED_Q_Q()
