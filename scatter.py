'''
Scatter sorting algorithm
Based on the distribution of values from a sample set, each 
element can be placed at/near its correct position independantly 
of other elements.
'''

import random

random.seed(7)
size = 10000000
# x = [random.randint(1, size) for i in xrange(size)]
x = range(size)

random.shuffle(x)

# print 'sorted',len(sorted(x))

def scatterSort(l,sampleSize):
	# sample set 
	sample = l[:sampleSize]

	# crate new list
	newOrder = [None] * len(l)

	# generage hash range
	hashEqu = lambda i:i

	for e in l:
		newOrder[hashEqu(e)] = e

	# interate through mix assigning each element into the new list based on the hash range
	return newOrder

print 'sorted',len(scatterSort(x,6))