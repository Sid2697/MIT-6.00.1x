def gcdRecur(a,b):
	'''
	a,b:positive integers
	
	returns a positive integer, the GCD of a and b
	'''
	if b==0:
		return a
	else:
		return gcdRecur(b,a%b)
