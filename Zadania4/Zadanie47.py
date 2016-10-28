# Python 2.7.4

fresh_seq = [1,(2,3),[],[4,(5,6,7)],8,[9],(10,11,(12,13,(14)))]

total_seq = []
def flatten(seq):


	for item in seq:
		if isinstance(item, (tuple, list)):
			item = flatten(item)
		else:
			total_seq.append(item)

	return total_seq

print flatten(fresh_seq)
