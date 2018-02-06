def getGuessedWord(secretWord,lettersGuessed):
	word = list()
	for letter in secretWord:
		if letter in lettersGuessed:
			word.append(letter)
		else:
			word.append(' _ ')
	return ''.join(word)
