
a=0
b=100
print('Please think of a number between 0 and 100!')
guess=(a+b)/2
while True:
	print('Is your secret number',guess,'?')
	inp=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	if inp=='c' or inp=='h' or inp=='l':
		if inp=='h':
			b=guess
			guess=int((a+b)/2)
		elif inp=='l':
			a=guess
			guess=int((a+b)/2)
		elif inp=='c':
			print('Game over. Your secret number was:',guess)	
			break	
	else:
		print('Sorry, I did not understand your input.')
