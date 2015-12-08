""" classes in python:
class name_of_class(object):
	
	def __init__(self):
	self.tangerine = "And now a thousand years between"
	
	def apple(self):
		print "I am classy APPLES!"
		
by instantiating you create objects from classes 
and you create a mini module, which you can assign to a variable, 
so you can work with it

"""
class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song([	"Happy birthday to you", 
					"I don't want to get sued",
					"So I'll stop here."])
					
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

print'--' * 10

bulls_on_parade.sing_me_a_song() 