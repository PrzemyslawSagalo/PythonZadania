# Python 2.7.4

d_symbol_value = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
d_symbol_value = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])


input = 'XCV'
total_value = 0

for i in range(len(input)):
	sing_input = input[i]
	value_input = d_symbol_value[sing_input]

	try:
		next_sing_input = input[i+1]
		next_value_input = d_symbol_value[next_sing_input]
		if next_value_input > value_input:
			value_input *= -1
	except IndexError:
		pass

	total_value += value_input
	# print value_input # line chcking singel value

print total_value
