# Python 2.7.4

LI = [0, 1, 2, 3, 4]

def odwracanie(L, left, right):
	par_l = L[left:right+1]
	par_l.reverse()

	L[left:right+1] = par_l

	return L

print odwracanie(LI, 1, 3)