# Python 2.7.4

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

print total
		