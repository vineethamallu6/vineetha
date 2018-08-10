'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print("Loading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = line.split()
	print("  ", len(wordlist), "words loaded.")
	return wordlist

def chooseWord(wordlist):
	"""
	wordlist (list): list of words (strings)

	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
def isWordGuessed(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list, what letters have been guessed so far
	returns: boolean, True if all the letters of secret_word are in letters_guessed;
	  False otherwise
	'''
	count = 0
	for i in secret_word:
		if i in letters_guessed:
			count += 1
	if count == len(secret_word):
		return True
	return False
def getGuessedWord(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list, what letters have been guessed so far
	returns: string, comprised of letters and underscores that represents
	  what letters in secret_word have been guessed so far.
	'''
	string = ''
	for i in secret_word:
		if i in letters_guessed:
			string = string + i
		else:
			string = string + '_'
	return string


def getAvailableLetters(letters_guessed):
	'''
	:param letters_guessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not
	  yet been guessed.
	'''
	import string
	DICT = string.ascii_lowercase
	st_r = ''
	for i in DICT:
		if i not in letters_guessed:
			st_r = st_r + i
	return st_r

def hangman(secret_word):
	'''
	secretWord: string, the secret word to guess.

	Starts up an interactive game of Hangman.

	* At the start of the game, let the user know how many 
	  letters the secretWord contains.

	* Ask the user to supply one guess (i.e. letter) per round.

	* The user should receive feedback immediately after each guess 
	  about whether their guess appears in the computers word.

	* After each round, you should also display to the user the 
	  partially guessed word so far, as well as letters that the 
	  user has not yet guessed.

	Follows the other limitations detailed in the problem write-up.
	'''
	# FILL IN YOUR CODE HERE...
	pass
	length = str(len(secret_word))
	letters_guessed = []
	guess = str
	mistakesMade = 8
	wordGuessed = False
	
	print('Welcome to the game, Hangman!')
	print('I am thinking of a word that is ' + length + ' letters long.')
	print('------------')

	while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
		if secret_word == getGuessedWord(secret_word, letters_guessed):
			wordGuessed = True
			break
		print('You have ' + str(mistakesMade) + ' guesses left.')
		print('Available letters: ' + getAvailableLetters(letters_guessed))
		guess = input('Please guess a letter: ').lower()
		if guess in secret_word:
			if guess in letters_guessed:
				print("Oops! You've already guessed that letter: " + getGuessedWord(secret_word, letters_guessed))
				print('------------')
			else:
				letters_guessed.append(guess)
				print('Good guess: ' + getGuessedWord(secret_word, letters_guessed))
				print('------------')
		else:
			if guess in letters_guessed:
				print("Oops! You've already guessed that letter: " + getGuessedWord(secret_word, letters_guessed))
				print('------------')
			else:
				letters_guessed.append(guess)
				mistakesMade -= 1
				print('Oops! That letter is not in my word: ' + getGuessedWord(secret_word, letters_guessed))
				print('------------')

	if wordGuessed == True:
		print('Congratulations, you won!')
	elif mistakesMade == 0:
		print('Sorry, you ran out of guesses. The word was ' + secret_word)


def main():
	'''
	Main function for the given program
	
	When you've completed your hangman function, uncomment these two lines
	and run this file to test! (hint: you might want to pick your own
	secretWord while you're testing)
	'''
	secret_word = chooseWord(wordlist).lower()
	hangman(secret_word)


if __name__ == "__main__":
	main()
