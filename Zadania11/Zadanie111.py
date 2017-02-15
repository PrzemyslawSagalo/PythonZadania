import random
from scipy.stats import truncnorm
import numpy as np
import matplotlib.pyplot as plt

def bubbleSort(alist):
    """
    Sortowanie buble sort ale wykonwane do polowy. Funkcja potrzebna do wygenerowania ciagow PRAWIE posortowanych.
    """
    for passnum in range(len(alist) - 1, len(alist)/2, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

    return alist

def rand_1(N, k):
    # lista k ROZNYCH liczb od 0 do N-1

    return random.sample(range(N), k)
# test
# print rand_1(50,5)

def rand_2(N):
    # rozne liczy od 0 do N-1 prawie posortowane
    list = range(N-1,-1,-1)
    list = bubbleSort(list)

    return list
# test
# print rand_2(10)

def rand_2_rev(N):
    # rozne liczby prawie posortowane w odwrotnej kolejnosci
    return rand_2(N)[::-1]
# test
# print rand_2_rev(10)

def rand_x(zbior_liczb, N):
    # N liczb w kolejnosci losowej, o wartosciach powtarzajscych sie, nalezacych do zbioru k elementowego (k < N, np. k*k = N)
    temp = []

    for i in range(N):
        temp.append(random.choice(zbior_liczb))

    return temp
# Test
# print rand_x([2, 2, 3, 4, 5], 9)


def rand_int_gauss(N, k):
    # N liczb z rozkladu gaussa
    scale = 3.
    range = k
    size = N

    X = truncnorm(a=-range / scale, b=+range / scale, scale=scale).rvs(size=size)
    X = X.round().astype(int)

    return X
# # Kod testujacy rand_int_gauss
nums = rand_int_gauss(10000,5)
print nums
bins = 2 * 10 + 1
plt.hist(nums, bins = bins)
plt.show()
