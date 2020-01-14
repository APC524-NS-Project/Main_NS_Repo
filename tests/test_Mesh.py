import unittest
import numpy as np
from src import mesh

class testMesh(unittest.TestCase):
	def setUp(self):
		test_shape = (2,4,3)
		self.mesh = mesh.Mesh(test_shape)

		#attach correct values of the mesh for the given shape
		self.zgrid = np.array([[[0,0,0],
							[0,0,0],
							[0,0,0],
							[0,0,0]],
							[[1,1,1],
							[1,1,1],
							[1,1,1],
							[1,1,1]]])
		self.ygrid = np.array([[[0,0,0],
								[1,1,1],
								[2,2,2],
								[3,3,3]],
								[[0,0,0],
								[1,1,1],
								[2,2,2],
								[3,3,3]]])
		self.xgrid = np.array([[[0,1,2],
								[0,1,2],
								[0,1,2],
								[0,1,2]],
								[[0,1,2],
								[0,1,2],
								[0,1,2],
								[0,1,2]]])

	def test_gen_grid(self):
		self.array_equal(self.mesh.meshes[0],self.zgrid)
		self.array_equal(self.mesh.meshes[1],self.ygrid)
		self.array_equal(self.mesh.meshes[2],self.xgrid)

	def test_slice(self):
		slices = ((0,2),(0,2),(1,3))
		keys = tuple((slice(*slc) for slc in slices))

		sliced = self.mesh.slice(slices)
		self.array_equal(sliced[0],self.zgrid[keys])
		self.array_equal(sliced[1],self.ygrid[keys])
		self.array_equal(sliced[2],self.xgrid[keys])

	def test_subslice(self):
		slices = ((0,2),(0,2),(1,3))
		keys = tuple((slice(*slc) for slc in slices))

		new_mesh = self.mesh.sub_slice(slices)
		self.array_equal(new_mesh.meshes[0],self.zgrid[keys])
		self.array_equal(new_mesh.meshes[1],self.ygrid[keys])
		self.array_equal(new_mesh.meshes[2],self.xgrid[keys])

		slices = ((None,),(None,),(1,3))
		keys = tuple((slice(*slc) for slc in slices))

		new_mesh = self.mesh.sub_slice(slices)
		self.array_equal(new_mesh.meshes[0],self.zgrid[keys])
		self.array_equal(new_mesh.meshes[1],self.ygrid[keys])
		self.array_equal(new_mesh.meshes[2],self.xgrid[keys])


	def array_equal(self,ar1,ar2):
		np.testing.assert_array_equal(ar1,ar2)