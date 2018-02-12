def iterPower(base,exp):
	ans=1
	while exp>0:
		ans=ans*base
		exp-=1
	return ans

