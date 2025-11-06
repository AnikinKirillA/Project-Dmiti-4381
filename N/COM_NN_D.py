def COM_NN_D(self, other):
    """
    Сделал: Соколовский Артём
    Сравнение двух натуральных чисел (self и other).
    Возвращает:
        2 — если self > other
        0 — если self == other
        1 — если self < other
    """
    A = self.A[:]
    B = other.A[:]

    while len(A) > 1 and A[0] == 0:
        A.pop(0)
    while len(B) > 1 and B[0] == 0:
        B.pop(0)

    if len(A) > len(B):
        return 2
    elif len(A) < len(B):
        return 1

    for da, db in zip(A, B):
        if da > db:
            return 2
        elif da < db:
            return 1

    return 0
