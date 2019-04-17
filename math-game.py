# A game that shows users a simple arithmetic question and a time limit to answer the greatest number of math questions possible

######################### ADD TIMER TO MAIN LOOP ########################

######################### LINK TO A BASIC DATABASE TO STORE ALL TIME BEST SCORES #########################

def timer():
	"""
	Function that will measure the time limit for the game.

	Will probably be 3 minutes or something of that sort
	"""
	import time

	t = 3
    
	while t:
		time.sleep(1)
		t -= 1
	return False
##################################### E N D   D E F ##########################################

def user_input():
	"""
	Handles user input and handles error in case a non-int is inputted
	"""
	while True:
		try:
			usr_in = int(input('Answer:\t'))
			break
		except:
			print('Not a number')
			print("Be careful! You're running out of time!")

	return usr_in
##################################### E N D   D E F ##########################################

def problem():
	"""
	Function that decides at pseudo-random which problem will be given with the ints 1 through 4

	# Returns variable 'verdict' to use for counting how many correct and incorrect answers we have in the main game loop
	"""
	import random

	# lambda used to provide the numbers to be used in the problem
	number = lambda: random.randint(0, 10)

	prob = random.randint(1, 4)
	x = number()
	y = number()

	if prob == 1:
		# Addition

		z = x + y

		# 'prob_str' is going to be used to store in a dictionary
		prob_str = f'{x} + {y}'
		print(prob_str)

		answer = user_input()

		verdict = z == answer

		print(f'Your answer: {answer}\nCorrect answer: {z}\n')
        
		return prob_str, verdict
###################################### E N D   I F  ##########################################

	elif prob == 2:
		# Subtraction
        
        # Eliminating the possibility of getting a negative number by setting it higher than 'y'
		if x < y:
			x = y + 1
            
		z = x - y

		# 'prob_str' is going to be used to store in a dictionary
		prob_str = f'{x} - {y}'
		print(prob_str)

		answer = user_input()

		verdict = z == answer

		print(f'Your answer: {answer}\nCorrect answer: {z}\n')
        
		return prob_str, verdict
###################################### E N D   I F  ##########################################

	elif prob == 3:
		# Multiplication

		z = x * y

		# 'prob_str' is going to be used to store in a dictionary
		prob_str = f'{x} x {y}'
		print(prob_str)

		answer = user_input()

		verdict = z == answer

		print(f'Your answer: {answer}\nCorrect answer: {z}\n')
        
		return prob_str, verdict
###################################### E N D   I F  ##########################################

	elif prob == 4:
		# Division

		########### Have to work on this. Float numbers are generally hard to get by mind #############

		# Division by 0 is not possible; adding 1 to prevent 0
		y += 1
        
		# Since it's x/y, setting x to a multiple of y within range of 0 to 10
		x = y * random.randint(1,10)
        
		z = x // y
            

		# 'prob_str' is going to be used to store in a dictionary
		prob_str = f'{x} / {y}'
		print(prob_str)

		answer = user_input()

		verdict = z == answer

		print(f'Your answer: {answer}\nCorrect answer: {z}\n')
		return prob_str, verdict
###################################### E N D   I F  ##########################################
##################################### E N D   D E F ##########################################

# Dictionary that holds the problems asked as key and the results as the value
history = dict()

# Stores the amount of questions that were asked before time ran out
num_questions = 0

# This will control the game loop.
#time = timer()

#while time != False:

# Counter for the while loop
# Temporary, will remove to be replaced with a while timer() and
# end that timer function with a return False to break out of this loop
x = 10

while x:
	# problem() function returns a tuple
    # prob_str is the problem that was asked and verdict is the outcome (correct or incorrect)
	prob_str, verdict = problem()
	history[prob_str] = verdict
    

	num_questions += 1
	x -= 1

# Counting the number of correct and incorrect answers
correct = 0
incorrect = 0

# Changing from True/False to 'Correct'/'Incorrect' and printing the answer
for k, v in history.items():
    if v:
        v = 'Correct'
        correct += 1
        
    else:
        v = 'Incorrect'
        incorrect += 1
        
    print(k, v)
    
print(f'\nOut of {num_questions} questions, you got {correct} right and {incorrect} wrong.')
print('You got an averege of: ', int((correct / num_questions)*100), '%')

"""
Testing threading instead of using time.sleep(). Threading wont affect the
use of the program like time.sleep() which interrupts the process until
the specified time interval

from threading import Timer

def rev():
    return 0

x = rev

t = Timer(2.0, rev)
t.start()
print(x)
"""
