import random
import dis

def birth(count):
	sameCount = 0
	for j in xrange(1000):
		for i in xrange(count):
			if random.randint(0, 364) == 7:
				sameCount += 1
				break
	return sameCount/1000.0

def mbirth(count):
	return 1-(364.0/365)**count

print birth(1650), mbirth(1650)

dis.dis(birth)