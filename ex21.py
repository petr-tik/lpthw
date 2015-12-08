def add(a,b):
	print "Adding %d to %d" % (a,b)
	return a + b

def substract(a,b):
	print "Taking %d away from %d" % (b,a)
	return a - b

def multiply(a,b):
	print "Multiplying %d by %d" % (a,b)
	return a*b


def divide(a,b):
	print "Dividing %d by %d" % (a,b)
	return a / b
	
print "let's do maths with functions!"

age = add(20,3)
height = substract(180,5)
weight = multiply(13,5)
iq = divide(200,2)

print "I am %d years old, my body weighs %d kilos and is %d cms tall, and I command it with my brain, whose iq is %d" % (
age, weight, height, iq)

# a puzzle 
print "Here is a puzzle"

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can I show it by hand?"  

# the solution lies in right-headedness of embedded functions
# if one function is embedded inside another you evaluate the former 
# and use its value to evaluate the latter

# no function returns or saves any results unless you explicitly tell it to
