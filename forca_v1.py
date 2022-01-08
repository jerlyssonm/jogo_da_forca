# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos dsa
import random

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class Hangman:

	def __init__(self, word):
		self.word = word
		self.misses_letter = []
		self.accept_letter = []

	def guess(self, letter):
		if letter in self.word and letter not in self.accept_letter:
			self.accept_letter.append(letter)
		elif letter not in self.word and letter not in self.misses_letter:
			self.misses_letter.append(letter)
		else:
			return False
		return True

	def hangman_over(self):
		return self.hangman_won() or (len(self.misses_letter) == 6)
		
	def hangman_won(self):
		if '_' not in self.hide_word():
			return True
		return False

	def hide_word(self):
		last_word = ''
		for letter in self.word:
			if letter not in self.accept_letter:
				last_word += '_'
			else:
				last_word += letter
		return last_word
		
	def print_game_status(self):
		print(board[len(self.misses_letter)])
		print('\nPalavra: '+ self.hide_word())
		print('\nLetras Erradas: ',)
		for letter in self.misses_letter:
			print(letter,)
		print()
		print('Letras Erradas: ',)
		for letter in self.accept_letter:
			print(letter,)
		print()

def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()

def main():

	game = Hangman(rand_word())

	while not game.hangman_won():
		game.print_game_status()
		user_input = input('\nDigite uma letra: ')
		game.guess(user_input)

	game.print_game_status()	

	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')
	
if __name__ == "__main__":
	main()