import random

print('Hello, what is your name?')
name = input()

secretNumber = random.randint(1,20)
print('Hello ' + name + ', I am thinking of a number between 1 and 20')

for guessesTaken in range(1, 7):
	print ("Take a guess:")
	guess = int(input())
	if guess < secretNumber:
		print ('Your guess is too low')
	elif guess > secretNumber:
		print ('Your guess is too high')
	else:
		#this condition is for the correct guess
		break
if guess == secretNumber:
	print('You got it ' + name + '!')	
	print('It took you  ' + str(guessesTaken) + ' guesses to get my number!')
else:
	print('Sorry, the number i was thinking of was ' + str(secretNumber))