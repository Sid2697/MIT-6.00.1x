def gcdIter(a,b):
	'''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
	'''
	if a<b:
		test=a
		sub=b
	else:
		test=b
		sub=a
	while test > 0:
		if ( a % test ==0 )and (b % test ==0):
			return test
			break
		elif test==1:
			return 1
		else:
			test-=1
