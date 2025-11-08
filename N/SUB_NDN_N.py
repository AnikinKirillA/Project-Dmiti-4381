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
Project-Dmit/N/SUB_NDN_N.py Project-Dmit/N/MUL_ND_N.py Project-Dmit/N/ADD_1N_N.py