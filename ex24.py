print "let's practice everything!"
print 'You\'d need to need to know \'bout escapes with \\ that do \nnew lines and \ttabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""
print "------------"
print poem
print "------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
# using a function we can determine the value of multiple variables
# the number of variables on the left has to match 
# the number of variables returned by the function 
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars and %d crates" % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars and %d crates." % secret_formula(start_point)