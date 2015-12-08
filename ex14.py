from sys import argv
script, user_name, age = argv
prompt = "talk dirty to me ... "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

computer = raw_input("What kind of computer do you have %s: " % user_name)

started_progr = int(raw_input("At what age did you start programming? "))

time_progr = int(age) - started_progr

print """
Alright, so you said %r about liking me. 
You live in %r. Not really sure where that is, I hope it's nice.
And you have a %r computer. It must be expensive

You have been coding for %s years.
""" % (likes, lives, computer, time_progr)
 