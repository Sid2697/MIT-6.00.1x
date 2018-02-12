def oddTuples(aTup):
	b=()
	c=()
	d=0
	for i in aTup:
		if d%2==0:
			b=b+(aTup[d],)
		else:
			c=c+(aTup[d],)	
		d+=1
	return b
