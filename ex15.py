# -*- coding: utf-8 -*-

# import argv function from sys library/module
from sys import argv

# assigns 2 argument variables script and filename
script, filename = argv

# assigns the variable txt the value of contents of 
# the file passed as argument into the script
txt = open(filename)

# print the name of the file
print "Here is your file: %r" % filename
# read the file out loud
print txt.read()

"""
# prints a string
print "Type the filename again:"
# prompts the user to manually enter the name of the text file
file_again = raw_input("> ")

# assigns the value of contents of the file, whose name the user had put in manually 
txt_again = open(file_again)
# prints the result of function read performed on txt_again file
print txt_again.read()

"""


# if you open a file, close it when you are done
txt.close()
txt_again.close()