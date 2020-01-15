import unittest
from src import plot_end
import mock
import numpy as np

class testPlotEnd(unittest.TestCase):
	def setUp(self):
		self.plot = plot_end.PlotEnd(r"tests/test_outs/")
		self.log = Logger()

	def test_plot1d(self):
		self.plot.plot1d(self.log,"test1")


class Logger():
	def __init__(self):
		self.grid = Grid()

	def get_frame(self,i):
		return [0,self.grid]

class Grid():
	def __init__(self):
		self.spec = mock.Mock()
		self.spec.coords = (0,1,2,3,4,5)
		self.spec.ndim = 1
		self.grid = np.array([5,4,3,2,1,0])
