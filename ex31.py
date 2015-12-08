door = int(raw_input("You are standing in front of two doors. Which door will you go through? "))

if door == 1:
	print "There is a giant bear eating cheese cake. What will you do?" 
	print "1. Take the cake"
	print "2. Scream at the bear"

	bear = int(raw_input("> "))
	
	if bear == 1:
		print "The bear eats your head"
	elif bear == 2:
		print "the bear eats your legs"
	else:
		print "Stop being funny, you only have 2 options. He will eat you" 

elif door == 2:
	print "You open the door and 3 naked women greet you"
	woman = int(raw_input("Which one will you pick? "))
# writing in the line now	
	if woman == 1:
		print "she is actually a thai ladyboy"
	elif woman == 2:
		print "\ashe is a suicide bomber - BOOM"
	elif woman == 3:
		print "That is your girlfriend Ana! Yay!"
	else:
		print "indecisiveness kills too"	  	
	
elif door == 3:
	print "well done, you saw the invisible door #3 - you are safe!"
	
else:
	print "indecisiveness kills too"
