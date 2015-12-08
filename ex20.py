# -*- coding=utf-8 -*-

# import argv from sys module
from sys import argv

# defines script and input file as script arguments
script, input_file = argv

# defines a function with 1 variable
def print_all(f):
# prints the whole file
	print f.read()

# defines a function with the same variable as the previous function	
def rewind(f):
# finds the position of 0 bytes in file f i.e. returns to the beginning of the file
	f.seek(0)

# defines a function with 2 variables: line number and file
def print_a_line(line_count, f):
# returns line number followed by a line
# readline reads just one line from file, readlines reads the whole line 
	print line_count, f.readline()
	
# read the input_file into a variable called current_file
	
current_file = open(input_file)

# prints a string and returns a new line

print "First, let's print the whole file:\n"

# calls function print_all and passes current_file as argument into the function
print_all(current_file)
# print a string
print "Now, we will rewind, kind of like a tape"
# calls the rewind function on current_file argument
rewind(current_file)
# print a string
print "Print 3 lines:"
# creates a loop
for i in range(1,4):
# at every repeat pass the i as argument into the print_a_line function
	print_a_line(i, current_file)
	
