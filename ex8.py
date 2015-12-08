# -*- coding: utf-8 -*-

# assigns a string value with 4 formatters to the variable formatter
formatter = "%r %r %r %r"

# prints the value of the variable formatter 
# passing four integer values into the string
print formatter % (1, 2, 3, 4)
# prints the value of the variable formatter 
# passing 4 string values into the string
print formatter % ("one", "two", "three", "four")
# prints the value of the variable formatter 
# passing 4 boolean values into the string
print formatter % (True, False, False, True)
# prints the value of the variable formatter 
# passing the value of the variable formatter into the string each time
print formatter % (formatter, formatter, formatter, formatter)
# prints the value of the variable formatter 
# passing 4 string values into the string. 
# The indents and separate lines make no difference to the way it's printed  
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

# while 3 strings are printed with ''
# the 3rd string is printed with "" to include the ' in don't

# assigns a string value with 3 formatters universal, string, decimal
# inside to variable formatter2
formatter2 = '%r %s %d'

# prints the value of formatter2 passing 3 appropriate variables 
# i.e. printed as shown  
print formatter2 % (True, "Hello World!", 15)
# prints the value of formatter2 passing 3 values
# printed showing the decimal representation of False 0
print formatter2 % (15, 15, False)
# prints the value of formatter2 passing 3 values
# printed 
print formatter2 % (15, False, True)
