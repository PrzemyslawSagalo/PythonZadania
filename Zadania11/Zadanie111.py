import random
from scipy.stats import truncnorm
import numpy as np
import matplotlib.pyplot as plt


def rand_1(N, k):
    # lista k ROZNYCH liczb od 0 do N-1

    return random.sample(range(N), k)
# # test
# print rand_1(50,5)

# rozne liczy od 0 do N-1 prawie posortowane

# rozne liczby prawie posortowane w odwrotnej kolejnosci


def rand_int_gauss(N, k):
    # N liczb z rozkladu gaussa
    scale = 3.
    range = k
    size = N

    X = truncnorm(a=-range / scale, b=+range / scale, scale=scale).rvs(size=size)
    X = X.round().astype(int)

    return X
# # Kod testujacy rand_int_gauss
# nums = rand_int_gauss(10000,5)
# print nums
# bins = 2 * 10 + 1
# plt.hist(nums, bins = bins)
# plt.show()


def rand_x(zbior_liczb, N):
    # N liczb w kolejnosci losowej, o wartosciach powtarzajscych sie, nalezacych do zbioru k elementowego (k < N, np. k*k = N)
    temp = []

    for i in range(N):
        temp.append(random.choice(zbior_liczb))

    return temp
# # Test
# print rand_x([2, 2, 3, 4, 5], 9)
