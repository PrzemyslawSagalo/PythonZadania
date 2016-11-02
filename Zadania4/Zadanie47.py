# Python 2.7.4

test_seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]

def flatten(seq):
	if isinstance(seq, (list,tuple)):
		if len(seq) == 0:
			return []
		first, second = seq[0], seq[1:]
		return flatten(first) + flatten(second)
	else:
		return [seq]

print flatten(test_seq)
