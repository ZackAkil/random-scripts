def e(w,h,cc,hc,wc):
	"""Print 'E' with given specs"""
	print((cc+wc*w+cc+'\n')+(((hc+'\n')*h)+(cc+wc*w+cc+'\n'))*2)

e(7,2,'@','|','-')


