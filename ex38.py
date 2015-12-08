# -*- coding=utf-8 -*-

# assign(ten_things, all the values in string
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are fewer than 10 items. Let's fix that!"

# split(list, character to split by)
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	# assign(pop(more_stuff)) 
	# assigns the value popped out of more stuff to next_one
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	# append(list, value)
	# appends a value to a list
	stuff.append(next_one)
	print "There are now %d items in the list" % len(stuff)
	
print "There we go: ", stuff

print "Now doing stuff to stuff"

# prints the second item in stuff list
print "%s is the second item in the list." % stuff[1]
# prints
print "%s is the last item in the list" % stuff[-1]

# removes the last item from the list
print stuff.pop()
print ' '.join(stuff)
print ', '.join(stuff[3:5]) 