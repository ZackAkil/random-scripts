def do(c):
	"""Get count of 7's in a range of numbers"""
    t = 0
    for i in range(c+1):
            for num in str(i):
                    if num == '7':
                            t += 1
    return t

print(do(100))