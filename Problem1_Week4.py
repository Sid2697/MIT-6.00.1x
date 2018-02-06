HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
def getWordScore(word,n):
	score = 0
	if len(word) == n :
		for letters in word:
			score += SCRABBLE_LETTER_VALUES[letters]
		score = score*len(word)
		score += 50
		print(score)
	else: 
		for letters in word:
			score += SCRABBLE_LETTER_VALUES[letters]
		score = score*len(word)
		print(score)
