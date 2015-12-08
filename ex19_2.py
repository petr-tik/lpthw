def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Dude, that's enough for a party"
	if cheese_count > boxes_of_crackers:
		print "Though you do have more cheese than crackers"
	if cheese_count == boxes_of_crackers:
		print "You have a perfectly balanced amount"
	if cheese_count < boxes_of_crackers:
		print "You have more crackers, get more cheese!"
		
cheese_count = int(raw_input("How many types of cheese do you have? "))
crackers_count = int(raw_input("How many boxes of crackers do you have? "))

cheese_and_crackers(cheese_count, crackers_count)


# you can also pass raw_input functions with prompts inside your original function
# that way you don't need to create and store variables
cheese_and_crackers(int(raw_input("How many cheeses? ")), int(raw_input("how many boxes of crackers? ")))


# variables defined and stored inside the functions 
# are not accessible outside the function
