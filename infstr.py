import operator
def infstr(s):
	a=map(ord,s)
	m=lambda x,y:x-y
	t=lambda i,j:i*j   
	return reduce(t,map(m,a[:3:2],a[1::2]))<0

print infstr('alpha')