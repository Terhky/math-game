# A game that shows users a simple arithmetic question and a time limit to answer the greatest number of math questions possible


########### FIX THE TIMER SO YOU  DONT HAVE TO DIVIDE IN ORDER TO GET THE TIME ################

########### FIX THE FLOAT RESULTS IN DIVISION ################

########### COUNT THE NUMBER OF CORRECT/INCORRECT ANSWERS ################


def timer():
	"""
	Function that will measure the time limit for the game.

	Will probably be 3 minutes or something of that sort
	"""
	import time
	t = 3
    
    while t:
    	mins, secs = divmod(t, 60)
    	time.sleep(1)
    	t -= 1
    print("Done!")

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

		# 'prob_str' is going to be used to store as a history variable
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
        #if x < y:
         #   x = y + 1
            
		z = x - y

		# 'prob_str' is going to be used to store as a history variable
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

		# 'prob_str' is going to be used to store as a history variable
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

		# Division by 0 is not possible, in that case, re-shuffle the numbers and add 1 to prevent another 0
		if x == 0 or y == 0:
			x = number() + 1
			y = number() + 1

		z = x / y

		# 'prob_str' is going to be used to store as a history variable
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
timer()
"""
# Counter for the while loop
# Temporary, will remove to be replaced with a while timer() and
# end that timer function with a return False to break out of this loop
x = 10

while x:
	# This function returns a tuple
    # prob_str is the problem that was asked and verdict is the outcome (correct or incorrect)
	prob_str, verdict = problem()
	history[prob_str] = verdict

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
    
print(f'Out of 10 questions, you got {correct} right and {incorrect} wrong.')
print('You got an average of: ', )
"""