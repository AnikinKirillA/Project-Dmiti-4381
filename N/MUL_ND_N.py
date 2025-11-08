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
