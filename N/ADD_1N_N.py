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
