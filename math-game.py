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

# Verify if the player's name is already in the highschore table
# Limit the number of highscores to 20 different players to save space
# Make a main menu in which you can pull your name from the txt to see your score

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
            c = int(input('1 = Yes/0 = No\t'))

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
        while len(name) < 1:
            name = input('Enter name:\t')
        
        # Have to format this string to accomdate for longer names.
        # Maybe hard code it to make it a max of 5 chars and space it accordingly?
        save_str = f'Score by: {name}  |  avg correct: {avg}%  |  num of questions: {num_questions}'
    
        # Have to format the saving in order of highest score to lesser score
        # This will be done with the value of avg
        # Make this value a float and to a 2 point decimal?
        with open("highscores.txt", "a") as fhand:
            print(save_str, file = fhand)
            
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
    avg = float((correct/num_questions)*100)
    
    # Outputting score results
    print(f'\nOut of {num_questions} questions, you got {correct} right and {incorrect} wrong.')
    print(f'You got an averege of: {avg}%')
    
    while True:
        try:
            print('\nWould you like to play again?')
            print('1 = Yes / 0 = No')
            c = int(input())   # c = choice
            
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
        
        # Not sure if this will help at all, but I think it might free upsome space,
        # instead of overwriting an existing value
        del correct
        del incorrect
        del num_questions
        del c
        del history
        del prob_str
        del verdict
        del avg
        
        print('\n'*2)
        play = False


print('Thanks for playing!')
# Working on the saving of data
# Need to check if the entered score is higher or lesser than the other info inside the highscore.txt file

# If it is then add one line above the higher score but below the score that is higher than itself
#(exception is if it's the top score)

# If the same user has a score already in the scoreboard and the new score is lower than the existing one
#then the score is added in it's rightful place following the previous rule

"""
# name of player
# num of questions completed
# avg score

name = 'Dood'
num_questions = 7
avg = 80.9
new_scr = f'{avg}%'

save_str = f'{avg}%   |   Score by: {name}   |   num of questions: {num_questions}'

def avg_catch(line):
    """
    Gets the avg to make a score out of it
    """   
    avg = line[6].split('%')
    avg = float(avg[0])
    
    return avg

with open('highscores.txt') as fhand:
    data = fhand.readlines()

# Sorting data from largest to smallest to get the top scores
data.sort(reverse=True)

for lines in data:
    lines = lines.split()
    
    # Replacing a previous lesser score
    if lines[2].lower() == name.lower():
        old_avg = avg_catch(lines)
        
        if old_avg < avg:
            lines[6] = new_scr
        else:
"""
