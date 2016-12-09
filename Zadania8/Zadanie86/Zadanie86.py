def dyn_P(i, j):
    """
    Wersja dynamiczna
    """
    if type(i) == int and type(j) == int and i >= 0 and j >= 0:
        P = {0:{0:0.5}}

        for i_ter in range(1,i+1):
            P[i_ter] = {0:0}
        for j_ter in range(1,j+1):
            P[0][j_ter] = 1

        for i_ter in range(1,i+1):
            # print 'i_ter', i_ter
            for j_ter in range(1,j+1):
                # print 'j_ter', j_ter
                P[i_ter][j_ter] = 0.5 * (P[i_ter - 1][j_ter] + P[i_ter][j_ter - 1])

        return P[i][j]

    else:
        raise ValueError

def rek_P(i, j):
    """
    Wersja rekurencyjna.
    """
    if type(i) == int and type(j) == int and i >= 0 and j >= 0:
        if i == 0 and j == 0:
            return 0.5
        elif j == 0:
            return 0
        elif i == 0:
            return 1
        elif i > 0 and j > 0:
            return 0.5 * (rek_P(i - 1, j) + rek_P(i, j - 1)) # i > 0, j > 0
    else:
        raise ValueError
