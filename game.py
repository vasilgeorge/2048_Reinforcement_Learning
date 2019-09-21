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
		for i in range(len(self.board)):
			self.board[i] = self.leftRowOperation(self.board[i])


	def move_right(self):
		for i in range(len(self.board)):
			self.board[i] = self.rightRowOperation(self.board[i])


	def move_up(self):
		for j in range(len(self.board[0])):
			self.board[:, j] = self.upColumnOperation(self.board[:, j])


	def move_down(self):
		for j in range(len(self.board[0])):
			self.board[:, j] = self.downColumnOperation(self.board[:, j])


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
         
		return addRow(row)


	@staticmethod
	def upColumnOperation(col):

		def addCol(col):
			col = compressCol(col)
			for i in range(len(col) - 1):
		            if col[i] == col[i + 1] and not np.isnan(col[i]):
		                    col[i] *= 2
		                    col[i + 1] = np.nan

			col = compressCol(col)
			return col

		def compressCol(col):
			for i in range(len(col)):
		            if np.isnan(col[i]):
		                    j = i+1
		                    while (j<len(col)):
		                            if not np.isnan(col[j]):
		                                    col[i], col[j] = col[j], col[i]
		                                    break
		                            j  += 1
		                    if j == len(col):
		                    	break
			return col

		return addCol(col)


	@staticmethod
	def downColumnOperation(col):
    	
		def addCol(col):
			col = compressCol(col)
			for i in reversed(range(len(col))):
				if col[i] == col[i-1] and not np.isnan(col[i]):
					col[i] *= 2
					col[i-1] = np.nan
			col = compressCol(col)
			return col


		def compressCol(col):
			for i in reversed(range(len(col))):
				if np.isnan(col[i]):
					j = i-1
					while (j>=0):
						if not np.isnan(col[j]):
							col[i], col[j] = col[j], col[i]
							break
						j  -= 1
					if j < 0:
						break
			return col
        
		col = addCol(col)       
		return col


game = Game()
print (game.board)
print('\n')
while not game.ended():
	
	move = np.random.randint(0, 4)
	if move==0:
		game.move_left()
		print("Moving left")
	elif move==1:
		game.move_right()
		print("Moving right")
	elif move==2:
		game.move_up()
		print("Moving up")
	else:
		game.move_down()
		print("Moving down")

	game.generate_new()
	print (game.board)
	print('\n')
print ('Game Over!')


