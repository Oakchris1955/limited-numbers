class Int:
	def __init__(self, number: int, limit: int, begin_from: int=0) -> None:
		self.number = number
		self.limit = limit
		self.begin_from = begin_from

	def _handle_update(self):
		'''Handles any number updates'''
		#if number is below limit
		if self.number < self.begin_from:
			#get the difference
			difference = self.begin_from-self.number
			#update the number
			self.number = self.limit-difference
		#if number is above limit
		elif self.number > self.limit:
			#get the difference
			difference = self.number-self.limit
			#update the number
			self.number = self.begin_from-difference

	def __add__(self, other:int) -> int:
		return self.number + other

	def __radd__(self, other:int) -> int:
		return self.number + other
	
	def __iadd__(self, other:int) -> None:
		self.number += other


	def __sub__(self, other:int) -> int:
		return self.number - other

	def __rsub__(self, other:int) -> int:
		return self.number - other
	
	def __isub__(self, other:int) -> None:
		self.number -= other