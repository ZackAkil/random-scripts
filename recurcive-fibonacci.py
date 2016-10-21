def fib(a):
	"""Recurcive fibonacci solution"""
	if a in [1,2]:
		return 1
	else:
		return fib(a-1) + fib(a-2)

print fib(10)