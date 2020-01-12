import unittest
from src import populator

class testPopulator(unittest.TestCase):
	def setUp(self):
		mock1 = mockSpec((2,4),1)
		inputs = ((mock1,0),)
		self.populs = (populator.Populator(inputs[0][0],inputs[0][1]),)

	#test _get_single_index method of populator
	def test_GSI(self):
		inputs = (([2,0],[0,1],[3,1]),)
		outputs_exp = ((2,4,7),)
		for idx,popul in enumerate(self.populs):
			for idx2,coord in enumerate(inputs[idx]):
				output = popul._get_single_index(coord)

				self.assertEqual(output,outputs_exp[idx][idx2])

class mockSpec():
	def __init__(self,shape,dx):
		self.shape = shape
		self.dx = dx
