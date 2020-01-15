import numpy as np
import scipy.sparse as sparse

## OperatorMatrix
# A Finite Difference Linear operator expressed as a matrix corresponding to the relevant combinations of values in a grid
class OperatorMatrix():
	## Constructor
	# initialize the operator matrix to be a sparse lil_matrix
	#
	# @param N dimensions of the matrix operator
	def __init__(self,N):
		self.shape = (N,N)
		self.array = sparse.lil_matrix(self.shape)
		self.populated = False

	## freeze_Op
	# method to convert internal storage from lil_matrix to a csr for better performance
	#
	# Call this method to transform the lil_matrix storage of the operator array to a csr_matrix storage to improve speed 
	# when evaluating operator. Additionally, set the populated Flag to true so that the operator knows it is populated
	def set_populated(self):
		self.array = sparse.csr_matrix(self.array)
		self.populated = True

	## __getattr__
	# Recast attribute calls to calls on the underlying array
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

	def __add__(self,other):
		if type(other) == OperatorMatrix:
			if other.shape == self.shape:
				new_op = OperatorMatrix(self.shape[0])
				new_op.array = self.array+other.array
				new_op.populated = True
				return new_op
			else:
				raise IndexError("Attempted to add two operators of different size.")
		else:
			raise TypeError("Attempted to add an OperatorMatrix to another object.")