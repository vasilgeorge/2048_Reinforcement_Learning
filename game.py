import numpy as np


class Game:

	def __init__(self):

		self.board = np.empty([4, 4])
		self.board[:] = np.nan

		first = np.random.randint(0, 4, 2)
		self.board[first[0]][first[1]] = self.get_random()

		second = np.random.randint(0, 4, 2)
		while second[0] == first[0] and second[1] == first[1]:
			second = np.random.randint(0, 4, 2)

		self.board[second[0]][second[1]] = self.get_random()


	def move_left(self):

		for row in self.board:
			_ = self.leftRowOperation(row)


	def move_right(self):

		for row in self.board:
			_ = self.rightRowOperation(row)


	# def move_up(self):

	# def move_down(self):

	def ended(self):
		return not np.isnan(self.board).any()

	def generate_new(self):

		new_cell = np.random.randint(0, 4, 2)

		while (not np.isnan(self.board[new_cell[0]][new_cell[1]])):
			new_cell = np.random.randint(0, 4, 2)

		self.board[new_cell[0]][new_cell[1]] = self.get_random()


	def get_random(self):

		prob = np.random.randint(0, 2, 1)
		return prob * 2 + (1 - prob) * 4

	# @static
	# def modified_addition(a, b):

	# 	if (a == b):
	# 		return a + b
	# 	else:
	# 		return np.nan

	@staticmethod
	def leftRowOperation(row):

		def addRow(row):
			row = compressRow(row)
			for i in range(len(row) - 1):
		            if row[i] == row[i + 1] and not np.isnan(row[i]):
		                    row[i] *= 2
		                    row[i + 1] = np.nan
			row = compressRow(row)
			return row

		def compressRow(row):
			for i in range(len(row)):
		            if np.isnan(row[i]):
		                    j = i+1
		                    while (j<len(row)):
		                            if not np.isnan(row[j]):
		                                    row[i], row[j] = row[j], row[i]
		                                    break
		                            j  += 1
		                    if j == len(row):
		                    	break
			return row

		row = addRow(row)
		return row


	@staticmethod
	def rightRowOperation(row):
    	
		def addRow(row):
			row = compressRow(row)
			for i in reversed(range(len(row))):
				if row[i] == row[i-1] and not np.isnan(row[i]):
					row[i] *= 2
					row[i-1] = np.nan
			row = compressRow(row)
			return row


		def compressRow(row):
			for i in reversed(range(len(row))):
				if np.isnan(row[i]):
					j = i-1
					while (j>=0):
						if not np.isnan(row[j]):
							row[i], row[j] = row[j], row[i]
							break
						j  -= 1
					if j < 0:
						break
			return row
        
		row = addRow(row)       
		return row


game = Game()
print (game.board)
print('\n')
while not game.ended():
	game.move_left()
	game.generate_new()
	print (game.board)
	print('\n')

print ('Game Over!')


