class Natural:
    def __init__(self, n, A):
        self.A = A #[] массив из int   123 -> [1, 2, 3]
        self.len = n #int len(A)-1

    def ADD_1N_N(self):
        """ 
        Выполнил: Сурин Максим 
        Добавление 1 к натуральному числу
        """
        
        """ 
        Запись числа справа налево;
        прибавление единицы к разряду единиц  
        """
        rev_num = self.A.copy()[::-1]
        rev_num[0] += 1

        """ Перенос единиицы при переполнении разряда """
        for i in range(self.len + 1):
            if rev_num[i] == 10:
                rev_num[i] = 0
                if i < self.len:
                    rev_num[i+1] += 1
                else: 
                    rev_num.append(1)
        
        return Natural(len(rev_num) - 1, rev_num[::-1])

    def MUL_ND_N(self, int):
        """ 
        Выполнил: Сурин Максим 
        Умножение натурального числа на цифру
        """
        
        """ Запись числа справа налево """
        rev_num = self.A.copy()[::-1]
        
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
                if i < self.len:
                    rev_num[i+1] += rev_num[i] // 10
                else: 
                    rev_num.append(rev_num[i] // 10)
                rev_num[i] %= 10
        
        return Natural(len(rev_num)-1, rev_num[::-1])

    def SUB_NDN_N(self, int, other):
        """ 
        Выполнил: Сурин Максим 
        Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом
        """

        """ Домножение второго числа на цифру """
        other_num = other.MUL_ND_N(int)

        """ В случае отрицательного результата возвращаем ноль """
        if self.COM_NN_D(other_num) == -1:
            return Natural(0, [0])
        
        return self - other_num
