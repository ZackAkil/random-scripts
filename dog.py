import random

def dog(count):
	unique= 0
	for i in range(count):
		week = [0,0,0,0,0,0,0]
		for d in range(4):
			born = random.randint(0, 6)
			week[born] = 1
		if sum(week)==4:
			unique += 1
	return unique*1.0/count


print dog(100000)