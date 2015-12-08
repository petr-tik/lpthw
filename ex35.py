# -*- coding=utf-8 -*-


from sys import exit
import random

# first room
def let_the_games_begin():	
	print "You are in a dark room with 2 doors"
	print "Which one will you open:\n\tleft \t\t\t\t\t\tright"
	
	choice = raw_input("> ")
	
	if "left" in choice:
		bear_room()
	elif "right" in choice:
		ctulhu_room()
	else:
		dead("You stumble around the room until starvation")

def dead(why):
	print why, "Good job, you are now dead!"
	exit(0)		

def bear_room():
	print "There is a bear here and he has a lot of honey"
	print "The fat bear is blocking a door\nHow are you going to move him?"
	
	bear_moved = False
	in_bear_room = True
	while in_bear_room == True: # changed to false when you open door
	
		choice = raw_input("Are you going to:\n\t\ttaunt bear\n\t\ttake honey\n\t\tmove bear\n> ")
		
		if "take honey" in choice: # lose
			dead("The bear looks at you and slaps your face off.")
		
		elif "taunt bear" in choice: # first step to unblock door
			bear_moved = random.choice([True, False])
			if bear_moved == True:
				print "The bear has moved from the door - you can squeeze past!"
			elif bear_moved == False:
				dead("The bear get pissed off.")
		
		elif "move bear" in choice:
			bear_moved = random.choice([True, False])
			if bear_moved == True:
				print "Success! You managed to move the bear!"
			elif bear_moved == False:
				dead("Shouldn't have touched him.")
		
		elif "open" in choice and bear_moved or "door" in choice and bear_moved:
			print "You clever thing!"
			in_bear_room = False
			gold_room()
		
		else:
			print "I have no idea what you said"

def gold_room():
	choice = int(raw_input("This room is full of gold. How much do you want? "))	
	print "You have decided to take %d units of gold" % choice
	
	if choice > 0 and 50 > choice:
		print "You have limits"
		
	elif choice > 50:
		dead("You greedy bastard")
	
	else:
		dead("Man, learn to type a number")
		
		
def ctulhu_room():
	print "Here you see the great evil Ctulhu"
	print "If he stares at you for too long, you will go mad"
	print "Do you want to?\n\t\tflee for your life\n\t\teat your head"
	choice = raw_input("> ")
	
	if "flee" in choice:
		let_the_games_begin()
	elif "head" in choice or "eat" in choice:
		dead("That was nutritious.")
	else:
		ctulhu_room()	

let_the_games_begin()