def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    #print("playGame not yet implemented.") # <-- Remove this when you code this function
    i=0
    while True:
    	choice=input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
    	if i==0 and choice == 'r':
    		print('You have not played a hand yet. Please play a new hand first!')
    		print(' ')
    		continue
    	if choice == 'n':
    		while True:
	    		choice1 = input('Enter u to have yourself play, c to have the computer play: ')
		    	HAND_SIZE = int(input('Enter the Hand Size: '))
    			if choice1 == 'u':
	    			hand=dealHand(HAND_SIZE)
    				playHand(hand,wordList,HAND_SIZE)
    				break
	    		elif choice1 == 'c':
	    			hand=dealHand(HAND_SIZE)
    				compPlayHand(hand,wordList,HAND_SIZE)
    				break
    			else:
    				print('Invalid command.')
    				continue
    		i+=1
    		continue
    	elif choice == 'r' and i != 0 :
    		while True:
	    		choice1 = input('Enter u to have yourself play, c to have the computer play: ')
	    		#HAND_SIZE = int(input('Enter the Hand Size: '))
	    		if choice1 == 'u':
	    			playHand(hand,wordList,HAND_SIZE)
	    			break
	    		elif choice1 == 'c':
	    			compPlayHand(hand,wordList,HAND_SIZE)
	    			break
	    		else:
	    			print('Invalid command.')
	    			continue
    		i+=1
    		continue
    	elif choice == 'e':
    		break
    	else:
    		print('Invalid command.')
