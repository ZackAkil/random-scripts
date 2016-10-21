def tri(v):
	"""Return triangle of asterisks"""
	return '\n'.join(map(lambda x:'*'*x,range(1,v)))

print(tri(10))