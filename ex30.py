#-*- coding=utf-8 -*-
people = 30
cars = 40 
trucks = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "we cannot decide"
	
if trucks > cars:
	print "That's too many trucks"
elif trucks < cars:
	print "maybe we could take the trucks"
else:
	print "we still cannot decide"

if people > trucks and cars == trucks:
	print "people can choose between cars or trucks"
else:
	print "there are either more trucks than people or the number of cars doesn't equal the number of trucks"
	
# if, elif (maybe multiple) and else assess which block of code should be run
# the elif statement with TRUE boolean value executes the block below it 
	
lines = [raw_input("line %d: " % i) for i in range (1,5)]
print lines