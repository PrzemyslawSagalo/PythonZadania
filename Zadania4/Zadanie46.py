# Python 2.7.4

def sum_seq(seq):
	val_sum = 0
	for el_seq in seq:
		if isinstance(el_seq, (list, tuple)):
			val_sum += sum(el_seq)
		else:
			val_sum += el_seq

	return val_sum


test_seq = [1,(2,3),[],[3,4]]

print sum_seq(test_seq)
