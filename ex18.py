# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is pointless, do this instead
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this one only needs 1 argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes NO arguments
def print_none():
	print "I got nothing' :-("
	

print_two("Zed", "lad")
print_two_again("Petr", "oh")
print_one(5)
print_none()

# all functions start with def
# then you name it
# in brackets you define how many variables it needs after brackets ':'
# indented below you describe what the function does using other functions 
# you close the function by dedenting

# calling a function by typing its name and brackets 
# with your variables (if needed) inside