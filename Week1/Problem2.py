s=input('Enter string: ')
length=len(s)
a=0
b=3
i=0
while a<=length and b<=(length+3):
	if s[a:b]=='bob':
		i+=1
	a+=1
	b+=1	
print("Number of times 'bob' occurs is:",i)
