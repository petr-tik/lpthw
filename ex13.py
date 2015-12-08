# -*- coding=utf-8 -*-

# add certain modules of sys into my script, keeps programmes small,
# otherwise, we would always load all modules without using them. redundant

from sys import argv

# argument variable holds all the variables 
# I will need to pass into my script later 



# takes x variables from the command line and passes them into the script

script, first, second, third = argv


# or you can ask the user to input them manually like above
print "your script is called:", script
print "the first variable is:", first
print "the second variable is:", second
print "the third variable is:", third


who_is_a_lad = raw_input("Is %r a lad? " % first)

