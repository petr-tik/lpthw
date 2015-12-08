# -*- coding=utf-8 -*-
the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of loop goes through list
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "a fruit of type: %s" % fruit

# also we can go through mixed lists
# notice we have to use %r since we don't know what type it is

for i in change:
	print "I have %r" % i


# building lists is also possible
elements = []

# then use the range function
# define the list as regexp
# pass i for i in range(x) 
elements = [i for i in range(6)]
	
# now we can print them out too
for i in elements:
	print "The element is: %d" % i
print elements

