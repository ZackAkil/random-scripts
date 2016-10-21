def brak(s):
	"""Validates the nesting of brackets"""
	depth = []
	topPlace = 0
	brakpair = {
				'}':'{',
				']':'[',
				')':'('
				}
	opens = brakpair.values()
	closes = brakpair.keys()

	for i in range(len(s)):
		l = s[i]

		if l in opens:
			if not depth:
				topPlace = i+1
			depth.append(l)

		elif l in closes:
			if not depth or depth.pop() != brakpair[l]:
				return str(i+1)
	if depth:
		return str(topPlace)
	return 'Success'

print brak('[dasasd]{sajkjh[csa(sas[as])]}asas[ss]')
