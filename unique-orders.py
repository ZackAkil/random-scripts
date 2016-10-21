def nest(l):
	"""Get all unique orders of a list without repeated elements"""
	if len(l) == 1:
		return l
	stacks = []
	for n in l:
		g = nest([x for x in l if x != n])
		if len(g) == 1:
			g.insert(0,n)
			stacks.append(g)
		else:
			for v in g:
				v.insert(0,n)
			stacks.extend(g)
	return stacks

print sorted(nest([2,3,0,8,9]))

