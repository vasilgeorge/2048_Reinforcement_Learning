from collections import defaultdict
import random


class ExperienceReplayMemory:


	def __init__(self):
		self.memory = defaultdict(int)


	def addExperienceToMemory(self, experience):
		self.memory[experience] = 1
		return


	def sampleMemory(self):
		return random.choice(list(self.memory.keys()))


	def getMemory(self):
		return self.memory