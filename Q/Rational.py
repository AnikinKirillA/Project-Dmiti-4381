from N.Natural import Natural
from Z.Integer import Integer
from TRANS.TRANS_N_Z import TRANS_N_Z


class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator #Integer числитель
        self.denominator = denominator #Natural знаменатель

    def RED_Q_Q(self):
        """
        Выполнил: Сурин Максим
        Сокращение дроби
        """

        """ 
        Приведение числителя к натуральному числу;
        вычисление НОД числителя и знаменателя;
        приведение НОД к виду целого числа
        """
        gcf = Natural(self.numerator.len, self.numerator.A).GCF_NN_N(self.denominator)
        gcf = Integer(0, gcf.len, gcf.A)

        new_ratio = self
        """ Если НОД не равен 1, сокращаем на него числитель и знаменатель """
        if gcf != 1:
            new_ratio.numerator = new_ratio.numerator // gcf
            new_ratio.denominator = new_ratio.denominator // gcf

        return new_ratio

    def INT_Q_B(self) -> bool:
        """
        Сделал: Захаренко Александр
        Проверка сокращенного дробного на целое,
        если рациональное число является целым,
        то «да», иначе «нет»
        """

        return self.denominator.A == [1]  # Знаменатель равен 1

    def ADD_QQ_Q(self, other):
        """
        Сделала: Имховик Наталья
        Выполняет сложение дробей
        Возвращает дробь
        """
        # Находим НОК знаменателей
        lcm = self.denominator.LCM_NN_N(other.denominator)

        # Находим дополнительные множители
        multiplyerA = lcm // self.denominator
        multiplyerB = lcm // other.denominator

        # Умножаем числители на дополнительные множители и складываем
        newNumerator = self.numerator * multiplyerA + other.numerator * multiplyerB

        # Создаем результирующую дробь
        return Rational(newNumerator, lcm)

    def SUB_QQ_Q(self, other):
        """
        Сделала: Имховик Наталья
        Находит разность дробей
        Возвращает дробь
        """
        # Находим НОК знаменателей
        lcm = self.denominator.LCM_NN_N(other.denominator)

        # Находим дополнительные множители
        multiplyerA = lcm // self.denominator
        multiplyerB = lcm // other.denominator

        # Умножаем числители на дополнительные множители и вычитаем
        newNumerator = self.numerator * multiplyerA - other.numerator * multiplyerB

        # Создаем результирующую дробь
        return Rational(newNumerator, lcm)

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

        return result

    def __truediv__(self, other):
        """
        Сделал: Чумаков Никита Ярославович
        Деление рациональных чисел q1 / q2.
        Делитель q2 ≠ 0.
        Возвращает новый Rational.
        """
        # Проверим, что делитель не равен нулю (числитель делителя != 0)
        if all(d == 0 for d in other.numerator.A):
            raise ZeroDivisionError("Деление на ноль в рациональных числах")

        # По формуле: (a/b) ÷ (c/d) = (a*d) / (b*c) перемножаем
        new_numerator = self.numerator * TRANS_N_Z(other.denominator)
        new_denominator = self.denominator * other.numerator.ABS_Z_Z()

        # Формируем новое рациональное число
        result = Rational(new_numerator, new_denominator)

        return result
