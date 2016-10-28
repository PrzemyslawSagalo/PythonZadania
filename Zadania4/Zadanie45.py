# Python 2.7.4

LI = [0, 1, 2, 3, 4, 5]

def rev_iter(seq):
	"Odwracanie calej listy wersja iteracyjna"
	for i in range(len(seq)/2):
		new_first = seq[(len(seq)-1)-i]
		new_last = seq[i]
		seq[i] = new_first
		seq[(len(seq)-1)-i] = new_last

	return seq

def rev_rek(seq):
	"Odwracanie calej listy wersja rekurencyjna"
	if len(seq):
		return rev_rek(seq[1:]) + seq[:1]
	else:
		return []


def odwracanie(L, left, right, ver):
	"""Odwracanie wybranego fragmentu listy wersja zalezy od wartosci ver.
	ver='iter' - wersja iteracyjna, ver='rek' - wersja rekurencyjna"""

	L = list(L)

	par_l = L[left:right+1]
	
	if ver == 'iter':
		L[left:right+1] = rev_iter(par_l)
	elif ver == 'rek':
		L[left:right+1] = rev_rek(par_l)

	return L


# ----------------------------------------------------
# Test
rekurencyjnie = odwracanie(LI, 1, 3, 'rek')
iteracyjnie = odwracanie(LI, 1, 3, 'iter')


print 'Lista odwrocona rekurencyjnie', rekurencyjnie
print 'Lista odwrocona iteracyjnie', iteracyjnie