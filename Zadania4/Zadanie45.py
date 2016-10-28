# Python 2.7.4

LI = [0, 1, 2, 3, 4, 5]

def rev_iter(seq):
	for i in range(len(seq)/2):
		new_first = seq[(len(seq)-1)-i]
		new_last = seq[i]
		seq[i] = new_first
		seq[(len(seq)-1)-i] = new_last

	return seq

def rev_rek(seq):

	if seq:
		return rev_rek(seq[1:]) + seq[:1]
	else:
		return []

def odwracanie(L, left, right):
	par_l = L[left:right+1]
		
	L[left:right+1] = rev_rek(par_l)

	return L

print odwracanie(LI, 1, 3)