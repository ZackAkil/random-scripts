from multiprocessing import Process, Value

def loop(varp):
	o = 0
	for i in range(1,10000000):
		o += i
		if 250000 % i is 0:
			varp.value = i
	print o

def print_new(varp):
	old_varp = -1
	while old_varp < 125000:
		if old_varp != varp.value:
			print varp.value
			old_varp = varp.value
	print 'done stuff'

if __name__ == '__main__':

	v = Value('d',0.0)


	p = Process(target=loop, args=(v,))
	p.start()
	
	p2 = Process(target=print_new, args=(v,))
	p2.start()
	


	# p.join()
	# p2.join()
