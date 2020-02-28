def endsPy(input):
	x=input.lower()
	for char in x:
		if x.endswith('py'):
			return True
	return False