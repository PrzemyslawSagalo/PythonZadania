par_l = [1,2,3,4]

print range(len(par_l)/2), len(par_l)

for i in range(len(par_l)/2):
	new_first = par_l[(len(par_l)-1)-i]
	new_last = par_l[i]
	par_l[i] = new_first
	par_l[(len(par_l)-1)-i] = new_last

print par_l
