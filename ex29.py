people = int(raw_input("How many people are there? "))
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! the world is doomed."

if people > cats:
	print "Not many cats! the world is safe ... for now"

if people < dogs:
	print "THe world is drooled on!"

if people > dogs:
	print "The world is dry!"
# adds 5 to the current value of dogs
dogs += 5

if people >= dogs:
	print "People are greater or equal to dogs"

if people <= dogs:
	print "people are less than or equal to dogs"

if people == dogs:
# a branch is created, the branch is activated if true, skipped otherwise
	print "people are dogs"
	
# if only activates the code under it, if the statement is true
# if the code isn't indented, then the if statement becomes irrelevant
# changing values makes different outcomes