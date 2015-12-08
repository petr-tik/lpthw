# -*- coding: utf-8 -*-

"""print "how old are you?",
age = raw_input()
print "How tall are you in cm?",
height = raw_input()
print "How much do you weight in kg?",
weight = raw_input()

print "so you are %r years of age, %r cm tall and weigh %r kg" % (
	age, height, weight)
	
"""
# more concise
"""
age2 = int(raw_input("How old are you? "))
height2 = float(raw_input("How tall are you in m? "))
weight2 = float(raw_input("How much do you weigh in kg? "))
BMI = weight2/(height2*height2)

print "I take it you are about %s years of age and you have %s kilos",
print "spread along your %s metres, which makes your BMI about %s" % (age2, weight2, height2, BMI)

"""
# raw_input takes input without converting it.
# input converts the numbers you put in. However, it has security flaws,
# better use raw_input and convert 

# put a string prompt in brackets of input

# get TypeError: not all arguments converted during string formatting


day = raw_input("What day is it today? ")
game = raw_input("Did United win? ")
if game == "no":
	print "It will be a shit %s night" % day
if game == "yes":
	scorers = raw_input("Who scored? ")
	print "Awesome! Can't wait for MotD and I bet %s's goal is amazing" % scorers