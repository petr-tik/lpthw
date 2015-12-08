# -*- coding=utf-8 -*-

# creates a mapping of state to abbreviation
states = {
	'Oregon' : 'OR',
	'Florida' : 'FL',
	'California' : 'CA',
	'New York' : 'NY',
	'Michigan' : 'MI'
}

# create a basic set of states and some states in them
cities = {
	'CA' : 'San Francisco',
	'MI' : 'Detroit',
	'FL' : 'Jacksonville'
}

# add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "The capital of NY state is", cities['NY']
print "THe capital of Oregon is", cities['OR']

# print out some state abbreviations
print '-' * 10
print "The abbreviation for Michigan is: ", states['Michigan']
print "The abbreviation for FLorida is: ", states['Florida']

# do it by using 2 dictionaries
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated as %s" % (state, abbrev)
	
# print every city in every state
print '-' * 10
for abbrev, city in cities.items():
	print "The city of %s is in %s state" % (city, abbrev)

# now both at the same time
print ' - ' * 15
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
	state, abbrev, cities[abbrev])

print '-' * 10
# get an abbreviation by state that might not be in the dictionary
state = states.get('Texas')

if not state:
	print "Sorry, no Texas!"

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is: %s" % city