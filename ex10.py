# -*- coding: utf-8 -*-

# escape character \ allows you to make python think \# isn´t a character

# assigns string value that is tabbed to a variable 
tabby_cat = "\tI'm tabbed in."
# assigns a string to a variable. The string is line split using escape n
persian_cat = "I'm split\non a line."
# assigns a string to variable, with double escapes, only 1 slash is printed though
backslash_cat = "I'm \\ a \\ cat."

# assigns a long """ string with multiple lines. Inside tab escapes are inserted. 
# when several escapes are combined, the number of \ has to correspond to # of escapes

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "\nlad"


print "\bad"

new = "I can print \non a new line \n\tor even tabbed %r a %s \nand then\a ring a bell" 
print new % (1000, "year")
# when you pass escapes into string using formatters, 
# %r passes the string literally, while %s passes \n as an escape 
new2 = """What about passing some escapes as formatters:
%snew line? %r new line?"""
print new2 % ("\n", "\n")