# Python 2.7.4

def zadanie35():
	whole_line_str = '|'

	whole_line_num = '0'

	number = 12

	i = 0
	while i < number:
		whole_line_str += '....|'
		i += 1
		if i >= 1 and i <= 9:
			whole_line_num += '    {}'.format(i)
		elif i > 9:
			whole_line_num += '   {}'.format(i)	
		
	whole = whole_line_str + '\n' + whole_line_num
	return whole


def zadanie36():
	total = ''

	n_row = 3
	n_columns = 9

	row = 1

	while row <= n_row:
		# Tutaj generujemy linie z '+---'
		columns = 1
		while columns <= n_columns:
			total += '+---'
			columns += 1
		total += '+'
		total += '\n'

		# Tutaj generujemy linie z '|   '
		columns = 1
		while columns <= n_columns:
			total += '|   '
			columns += 1
		total += '|'
		total += '\n'

		row += 1

	# Generacja ostatniej linii '+---'
	columns = 1
	while columns <= n_columns:
		total += '+---'
		columns += 1
	total += '+'

	return total

print zadanie35()
print zadanie36()