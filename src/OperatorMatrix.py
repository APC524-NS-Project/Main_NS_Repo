import numpy as np

class OperatorMatrix():
	def __init__(self,N):
		self.shape = (N,N)
		self.array = np.zeros(self.shape)

	def __getattr__(self, name):
		try:
			return getattr(self.array, name)
		except AttributeError:
			raise AttributeError(
				"'OperatorMatrix' object has no attribute {}".format(name))

	def __getitem__(self, key): 
		return self.array.__getitem__(key)

	def __setitem__(self, key, value):
		self.array.__setitem__(key, value)

	def __str__(self):
		self.array.__str__()

	def __repr__(self):
		self.array.__repr__()
