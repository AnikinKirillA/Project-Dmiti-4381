def ADD_1N_N(self):
    """ 
    Выполнил: Сурин Максим 
    Добавление 1 к натуральному числу
    """
    
    rev_num = self.A.reverse() # Запись числа справа налево
    rev_num[0] += 1 # Прибавление единицы к разряду единиц

    """ Перенос единиицы при переполнении разряда """
    for i in range(self.len + 1):
        if rev_num[i] == 10:
            rev_num[i] = 0
            if i < self.len:
                rev_num[i+1] += 1
            else: 
                rev_num.append(1)
    
    return Natural(len(rev_num) - 1, rev_num.reverse())
