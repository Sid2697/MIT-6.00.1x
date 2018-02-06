def isWordGuessed(secretWord,lettersGuessed):
	secret = list()
	i=0
	for letter in secretWord:
		if letter in lettersGuessed:
			i+=1
	if len(secretWord)==i:
		return True
	else:
		return False
		
