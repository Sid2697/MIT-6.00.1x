def getAvailableLetters(lettersGuessed):
	alphabets= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for letter in lettersGuessed:
		if letter in alphabets:
			alphabets.remove(letter)
	return ''.join(alphabets)
