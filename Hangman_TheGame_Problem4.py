import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secret = list()
    i=0
    for letter in secretWord:
    	if letter in lettersGuessed:
    		i+=1
    if len(secretWord)==i:
    	return True
    else:
    	return False
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = list()
    for letter in secretWord:
    	if letter in lettersGuessed:
    		word.append(letter)
    	else:
    		word.append(' _ ')
    return ''.join(word)
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabets= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in lettersGuessed:
    	if letter in alphabets:
    		alphabets.remove(letter)
    return ''.join(alphabets)
def hangman(secretWord):
	lettersGuessed = list()
	numGuesses = 8
	print('Welcome to the game, Hangman!')
	print('I am thinking of a word that is',len(secretWord),'letters long.')
	while numGuesses>0:
		print('-------------')
		if numGuesses != 1:
			print('You have',numGuesses,'guesses left.')
		else:
			print('You have',numGuesses,'guess left.')
		availableLetters = getAvailableLetters(lettersGuessed)
		print('Available Letters:',availableLetters)
		inp=input('Please guess a letter: ')
		if inp not in lettersGuessed:
			lettersGuessed.append(inp)
		else:
			if inp in lettersGuessed:
				guessedWord = getGuessedWord(secretWord,lettersGuessed)
				print("Oops! You've already guessed that letter:",guessedWord)
				continue		
		if inp in secretWord:
			guessedWord = getGuessedWord(secretWord,lettersGuessed)
			print('Good guess: ',guessedWord)
		else:
			guessedWord = getGuessedWord(secretWord,lettersGuessed)
			print('Oops! That letter is not in my word:',guessedWord)
			numGuesses -= 1
		if '_' not in guessedWord:
			print('-------------')
			print('Congratulations, you won!')
			break
		if numGuesses==0 and '_' in guessedWord:
			print('-------------')
			print('Sorry, you ran out of guesses. The word was',secretWord,'.')

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
