# -*- coding=utf-8 -*-
i = 0
numbers = []
lad = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i += 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
	
print "The numbers: "
# might be empty, if only used and saved in while loop
# can take any arbitrary for x in y
for num in numbers:
	print num
	
def add_x_to_list(list,x,g):
	# list - is list, x is the number appended, 
	# g is the jump between the values of x
	lad = []
	print 'x = %d' % x
	print 'g = %d' % g
	for x in range(0, (x - 1), g):
		list.append(x)
	print list
	
add_x_to_list(lad, int(raw_input('How big is x? ')), int(raw_input('How big is the step? ')))