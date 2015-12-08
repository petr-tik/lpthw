# -*- coding: utf-8 -*-
# assigns the variable x a string value with a formatter 
# integer bringing 10 into the string when it's called
x = "There are %d types of people." % 10
# assigns the string value "binary" to variable binary
binary = "binary"
# assigns the string value "don't" to variable do_not
do_not = "don't"
# the variable y is assigned a string value into which 2 string formatters integrate the values of 2 variables:
# binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the value of the variable x once all the formatters have been replaced with the values of the variables 
print x
# prints the value of the variable y once all the formatters have been replaced with the values of the variables
print y

# prints a string and passes a formatter that converts the value of x into a string using repr() 
print "I said: %r." % x
# converts y in into a string using str() function
print "I also said: '%s'." % y

#assigns the variable hilarious a boolean value: False
hilarious = False
# assigns the variable joke_evaluation a string value with a conversion value %r at the end of the string 
joke_evaluation = "Isn't that joke so funny?! %r"

# converts the value of hilarious into a string using repr(), passes it into the string of joke_evaluation, 
# then prints the overall results
print joke_evaluation % hilarious

# assigns a string value to the variable w
w = "This is the left side of..."
# assigns a string value to the variable e
e = "a string with a right side."

# adds 2 strings together and prints the results 
print w + e

# adding 2 strings w and e, puts the first character of string e after the 
# last character of string w and the overall length is w + e 

# there are 6 places where a string is passed into another string:
# lines 10, 15, 18, 20, 25, 29