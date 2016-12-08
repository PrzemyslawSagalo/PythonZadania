def fun_P(i,j):
    i += 1
    j += 1
    P = {0:{0:0.5}}

    for i_ter in range(1,i):
        P[i_ter] = {0:0}
    for j_ter in range(1,j):
        P[0][j_ter] = 1

    for i_ter in range(1,i):
        # print 'i_ter', i_ter
        for j_ter in range(1,j):
            # print 'j_ter', j_ter
            P[i_ter][j_ter] = 0.5 * (P[i_ter - 1][j_ter] + P[i_ter][j_ter - 1])

    i -= 1
    j -= 1

    return P[i][j]

print fun_P(3,4)