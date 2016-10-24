with open('nam_dict.txt', 'r') as f:
 	for i in range(50000):
		read_data = f.readline().split(' ')
		gender = read_data[0]
		name = read_data[1] if read_data[1] else read_data[2]
		if '+' in name:
			name = name.replace('+',' ')
		print(gender,name,i)