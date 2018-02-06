def playGame(wordList):
	i=0
	while True:
		choice = print('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
		if i==0 and choice == 'r':
			print(You have not played a hand yet. Please play a new hand first!)
			continue
		if choice == 'n':
			hand=dealHand(HAND_SIZE)
			playHand(hand,wordList,HAND_SIZE)
			i+=1
			continue
		elif choice == 'r' and i != 0:
			playHand(hand,wordList,HAND_SIZE)
			i+=1
			continue
		elif choice == 'e':
			break
		else:
			print('Invalid command.')
			
