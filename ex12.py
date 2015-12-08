age2 = int(raw_input("How old are you? "))
height2 = float(raw_input("How tall are you in m? "))
weight2 = float(raw_input("How much do you weigh in kg? "))
BMI = weight2/(height2*height2)

print "I take it you are about %s years of age and you have %s kilos",
print "spread along your %s metres, which makes your BMI about %s" % (age2, weight2, height2, BMI)


"""
open opens any file
file can either read, write or append
os imports variables and functions already present in different oss
makes programmes cross-platform

sys module provides access to objects used or maintained by the terminal 


use %r it's raw! %s is good for display but useless for debugging. 
%r prints literals, which helps when debugging