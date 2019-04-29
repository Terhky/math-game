############# Make a main menu for score searching or sort by specifics like sort by avg% or num of questions ############


import threading

def timer():
    """
    Flag that represents when the game is to begin.
    """
    import time

    # 3 seconds to begin a countdown in order to let users know that the game will begin
    t = 3

    # 3...2...1
    while t:
        print(t, end='\r')
        time.sleep(1)
        t -= 1

    event.set()   # ...GO!

    # sleep will be the length of the game; a minute or more
    time.sleep(10)

    # End game flag
    
    print("Time's up!")
    
    print('Answer will not be counted towards score...')
    event.clear()
    
##################################### E N D   D E F ##########################################


def save_game(avg, num_questions):
    """
    Handles score saving.
    Limit of 20 scores in save data to save space.
    
    Checks the highscore table every time there is a save request to check if the name already exists on the list.
    If it is, then only overwrite it if the current score is higher than the one in the table. Otherwise add the
    lesser score to it's rightful position below the higher score
    """    
    while True:
        try:
            print('Save Score?')
            c = int(input('1 = Yes/0 = No\n'))

            if c == 1 or c == 0:
                break
            else:
                print(f'{c} is not a valid input\n')
                continue

        except:
            print(f'{c} is not a valid input\n')
            continue
            
    if c == 1:        
        name = ''
        while len(name) < 1 or len(name) > 5:
            print('Enter name...')
            name = input('Name must contain 1 character and be lesser than 5 characters long\n')
            
            if len(name) > 5:
                print('Invalid name...\n')
                continue
            
        save_str = f'{avg}%\t|\tScore by: {name}\t|\tnum of questions: {num_questions}\t|'
        
        with open('highscores.txt', 'r') as fhand:    
            scores = fhand.readlines()

        edit = scores   # Temp variable to be used to manipulate data
        save_str = save_str.split()
        save_str = '\t'.join(save_str)
        edit.append(save_str)
        
        # Added the current save data to the list and then checked the list elements to see if the playaer had history
        # If True then it will check if the old score is lesser or higher than the current score. If current is higher
        # then it will replace the older score. Otherwise it will be stored as a separate table entry
        for i, lines in enumerate(scores):
            lines = lines.split()

            old_name = lines[4].lower()
            
            if name.lower() == old_name:
                # Getting previous avg
                old_avg = lines[0].split('%')
                old_avg = float(old_avg[0])
                
                if avg > old_avg:
                    edit.pop(i)
                    break
                else:
                    break         

        scores = edit   # Overwriting scores to make storing easier

        # Limit of 20 entries in the table
        if len(scores) > 20:
            scores.pop()

        #Sorting by reverse to arrange from larger to lesser
        scores.sort(reverse = True)

        with open('highscores.txt', 'w') as fhand:
            for lines in scores:
                lines = lines.rstrip()
                print(lines)
                print(lines, file = fhand)
            
        print('\nSaved!')
        print(save_str)
    
    else:
        return
        
##################################### E N D   D E F ##########################################

def user_input():
	"""
	Handles user input and handles error in case a non-int is inputted
    
    While event is set to True run the user input and break to return answer.
    Otherwise the loop would run continuously.
    
    An additional if statement to check for event is added just in case the
    program enters the loop just after the time ends as a fail-safe.
    
    When False is returned, the question is omitted and not counted towards final score
	"""
    
	event.wait()
    
	while event.is_set():
		try:
			usr_in = int(input('Answer:\t'))
			break
		except:
			print('Not a number')
			print("Be careful!\nYou're running out of time!")

	if event.is_set():
		return usr_in
	else:
		return None
##################################### E N D   D E F ##########################################

def problem():
	"""
	Function that decides at pseudo-random which problem will be given with the ints 1 through 4
	Returns variable 'verdict' to use for counting how many correct and incorrect answers we have in the main game loop
	"""
	import random

	# lambda used to provide the numbers to be used in the problem
	number = lambda: random.randint(0, 10)

	prob = random.randint(1, 4)
	x = number()
	y = number()
    
###################################### S T A R T   I F  ##########################################
	if prob == 1:
		# Addition

		z = x + y

		prob_str = f'{x} + {y}'   # 'prob_str' is going to be used to store in a dictionary
        
        # Return carriage to overwrite the line and not clutter the screen
		print(prob_str)

		answer = user_input()
        
		if answer == None:
			verdict = answer
		else:
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

		prob_str = f'{x} - {y}'   # 'prob_str' is going to be used to store in a dictionary
        
        # Return carriage to overwrite the line and not clutter the screen
		print(prob_str)

		answer = user_input()
        
		if answer == None:
			verdict = answer
		else:
			verdict = z == answer

		print(f'Your answer: {answer}\nCorrect answer: {z}\n')
        
		return prob_str, verdict
###################################### E N D   I F  ##########################################

	elif prob == 3:
		# Multiplication

		z = x * y

		prob_str = f'{x} x {y}'   # 'prob_str' is going to be used to store in a dictionary
        
        # Return  carriage to overwrite the line and not clutter the screen
		print(prob_str)

		answer = user_input()
        
		if answer == None:
			verdict = answer
		else:
			verdict = z == answer

		print(f'Your answer: {answer}\nCorrect answer: {z}\n',)
        
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
            

		prob_str = f'{x} / {y}'   # 'prob_str' is going to be used to store in a dictionary
        
        # Return  carriage to overwrite the line and not clutter the screen
		print(prob_str)

		answer = user_input()
        
		if answer == None:
			verdict = answer
		else:
			verdict = z == answer

		print(f'Your answer: {answer}\nCorrect answer: {z}\n',)
		return prob_str, verdict
###################################### E N D   I F  ##########################################
##################################### E N D   D E F ##########################################

play = True # Main game loop control

while play:
    history = dict()    # Dictionary that holds the problems asked as key and the results as the value
    num_questions = 0   # Stores the amount of questions that were asked before time ran out

    event = threading.Event()   # Setting the event for the timer
    t1 = threading.Thread(target = timer)
    t1.start()   # Game start

    # Wait until event is set
    event.wait()

    while event.is_set():
        # problem() function returns a tuple
        # prob_str is the problem that was asked and verdict is the outcome (correct or incorrect)
        prob_str, verdict = problem()
        history[prob_str] = verdict

        num_questions += 1

    print('Game over!\n')

    # Counting the number of correct and incorrect answers
    correct = 0
    incorrect = 0
    

    # Counting results
    for k, v in history.items():
        if v:
            correct += 1

        elif v == False:
            incorrect += 1
        
        # If answer is None then subtract that question 
        else:
            num_questions -=1

        print(f'Problem: {k}\t\tResult: {v}')
    
    # Averege percent of correcft answers
    try:
        avg = float((correct/num_questions)*100)
    except:
        avg = 0
    
    # Outputting score results
    print(f'\nOut of {num_questions} questions, you got {correct} right and {incorrect} wrong.')
    print(f'You got an averege of: {avg}%')
    
    while True:
        try:
            print('\nWould you like to play again?')
            c = int(input('1 = Yes / 0 = No\t'))   # c = choice
            
            # Making sure that c isn't another number
            if c == 1 or c == 0:
                break
            else:
                print(f'{c} is not a valid input\n')
                continue
                
        except:
            print('Please make a valid input\n')
    
    if c == 1:
        print('\n'*2)
        continue
    else:
        save_game(avg, num_questions)
        
        print('\n'*2)
        play = False


print('Thanks for playing!')


"""

######### HAVE TO CONVERT AVG IN SCORES TO FLOAT IN ORDER TO ORGANIZE THEM PROPERLY
######### AS IT IS RIGHT NOW IT IS A STRING INSTEAD OF A NUMBER; REASON WHY 100 < 90

name = 'perl'
avg = 100
num_questions = 70

save_str = (f'{avg}%\t|\tScore by: {name}\t|\tnum of questions: {num_questions}\t|')

with open('highscores.txt', 'r') as fhand:    
    scores = fhand.readlines()

edit = scores   # Temp variable to be used to manipulate data
save_str = save_str.split()
save_str = '\t'.join(save_str)
edit.append(save_str)

# Checking to see if player has a previous score. If True then it will check if the current score
# is greater than the past one and if it is then it will be overwritten.

#If the current player does not have an old score then the lines variable which is used to write
# the scores into the edit list will be saved as the save_str format. Splitting 'lines' to make the
# join method look more uniform during output.
for i, lines in enumerate(scores):
    lines = lines.split()

    old_name = lines[4].lower()

    if name.lower() == old_name:
        # Getting previous avg
        old_avg = lines[0].split('%')
        old_avg = float(old_avg[0])

        if avg > old_avg:
            edit.pop(i)
            break
        else:
            break

for i, lines in enumerate(edit):
    lines = lines.split('%')
    lines = float(lines[0])
    
    scores[i] = lines

for lines in scores:
    print(lines)

# Limit of 20 entries in the table
if len(scores) > 20:
    scores.pop()


#Sorting by reverse to arrange from larger to lesser
scores.sort(reverse = True)


"""
