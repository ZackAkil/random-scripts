def exstring(s):
	"""Get list of unique character quantities for a string"""
	return [x*s.count(x)for x in set(s.replace(" ", ""))]

print exstring('Ah, abracadabra!')


