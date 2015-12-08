def break_words(stuff):
# this is documentation, you can pull it up if you help(name_of_script) 
	"""this function will break words up for us"""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""sorts the words"""
	return sorted(words)

def print_first_word(words):
	"""prints the first word after popping it off"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""prints the last word after popping it off"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""takes in a full sentence and returns the sorted words"""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""print the first and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""sorts the words and then prints the first and last"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	

	