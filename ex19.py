# -*- coding=utf-8 -*-

# variables inside functions are independent
# from variables in the rest of the script

# define the function and the variables inside the brackets
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# prints a string with a formatter that passes the value of the first variable
	print "You have %d cheeses" % cheese_count
# prints a string with a formatter that passes the value of the second variable
	print "You have %d boxes of crackers" % boxes_of_crackers
# prints a string	
	print "Dude, that's enough for a party"
# presents 3 options in the function
# if the value of cheese count is greater than boxes of crackers	
	if cheese_count > boxes_of_crackers:
	# print a string
		print "Though you do have more cheese"
# if the values are equal		
	if cheese_count == boxes_of_crackers:
	# prints a string saying that
		print "You have a perfectly balanced amount"
	# if there are more crackers	
	if cheese_count < boxes_of_crackers:
	# print a string
		print "You have more crackers, get more cheese!"
# prints a tabbed string on a new line
print "\t\nwe can directly give numbers as variables:"
# passes 2 numbers as variables into the function
cheese_and_crackers(20,30)

# prints a tabbed string on a new line
print "\n\tOR, we can use variables from our script:"
# sets the amount of cheese and crackers
amount_of_cheese = 10
amount_of_crackers = 50
# passes the variables into  
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# prints a tabbed line on anew string
print "\n\twe can even pass math formulae with integers as variables"
# calls a function with 2 calculations as arguments
cheese_and_crackers(10 + 20, 5 + 6)

# prints a tabbed string on a new line
print "\n\tor combine variables and maths:"
# passes 2 formulae using calculations between variables and constants
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers - 5)


