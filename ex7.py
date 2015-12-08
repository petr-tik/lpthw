# -*- coding: utf-8 -*-

# prints a string
print "Mary had a little lamb."
# use a formatter to pass another string inside the string and print the overall results
print "Its fleece was white as %s." % "snow"
# print a string
print "And everywhere that Mary went."
# repeat the action of printing 20 times. makes a buffer line
print "<>" * 20 # what'd that do?

# assigns the variable end1 string value "C"
end1 = "C"
# assigns the variable end2 string value "h"
end2 = "h"
# assigns the variable end3 string value "e"
end3 = "e"
# assigns string value "e" to the variable end4
end4 = "e"
# assigns string value "s" to the variable end5 
end5 = "s"
# assigns string value "e" to the variable end6
end6 = "e"
# assigns string value "B" to the variable end7
end7 = "B"
# assigns string value "u" to the variable end8
end8 = "u"
# assigns string value "r" to the variable end9
end9 = "r"
# assigns string value "g" to the variable end10
end10 = "g"
# assigns string value "e" to the variable end11
end11 = "e"
# assigns string value "r" to the variable end12
end12 = "r"

# first with the comma - prints 6 string values together, 
# inserts a space and prints the other 6 on the same line
# good style - fewer than 80 characters in one line
print end1 + end2 + end3 + end4 + end5 + end6, 
print end7 + end8 + end9 + end10 + end11 + end12

# now without the comma - prints one line adding the strings together, then prints another line of strings together
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12 

print "hue" * 20