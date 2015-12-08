## animal is-a object 

class Animal(object):
	pass
	
## Class Dog is-a Animal

	def __init__(self, name):
	# function __init__ has-a self and name parameters
	self.name = name
	
## 
class Cat(Animal):

	def __init__(self, name):
		## 
		self.name = name
		
## 
class Person(object):

	def __init__(self, name):
		##
		self.name = name
		
		## person has-a pet of some kind
		self.pet = None