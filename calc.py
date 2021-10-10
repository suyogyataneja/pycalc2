def compute(exp):
	values =exp.split(' ')
	num0 = int(values[0])
	operator = values[1]
	num1 = int(values[2])
	if operator == '+':
		return num0 + num1
	else:
		print('unkown operator')
		return  0

