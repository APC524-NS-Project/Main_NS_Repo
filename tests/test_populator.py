import unittest
from src import populator

class testPopulator(unittest.TestCase):
	def setUp(self):
		inputs = (((2,4),0,1))
		self.populs = (populator.Populator(inputs[0][0],inputs[0][1],inputs[0][2]))

	#test _get_single_index method of populator
	def test_GSI(self):
		inputs = (([0,2],[1,0],[3,1]),)
		outputs_exp = ((2,4,7))
		for popul, idx in enumerate(self.populs):
			for coord, idx2 in enumerate(inputs[idx]):
				output = popul._get_single_index(coord)

				self.assertEqual(output,outputs_exp[idx][idx2])
