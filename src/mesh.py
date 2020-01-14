import numpy as np

## Mesh
# A set of arrays generated from a base grid containing key value paris stored in matricies
#
# Generates a gridmesh for a given shape of base grid and then stores that as an n-dimensional tuple where n is the dimension of the base grid
class Mesh():
	## Constructor
	# 
	# @param shape A tuple of dimensions corresponding to the shape of the overlying grid we wish to generate a mesh for
	# @var self.base_shape Storage of the original shape of the mesh
	# @var dim dimensionality of the base grid
	def __init__(self,shape):
		self.base_shape = shape
		self.dim = len(self.base_shape)
		self._gen_grid()

	## _gen_grid
	# Private class run at startup to create the gridmeshes
	# 
	# For a given shape tuple generates the corresponding gridmesh
	# @var meshes tuple of arrays corresponding to the meshes in each dimension of the base grid
	def _gen_grid(self):
		gen_tup = tuple((range(n) for n in self.base_shape))
		self.meshes = tuple(np.meshgrid(*gen_tup,indexing='ij'))

	## __getitem__
	# Overwrite getitem method to return a tuple of values corresponding the the relevant item in each dimesnion's mesh
	def __getitem__(self,key):
		return tuple((mesh.__getitem__(key) for mesh in self.meshes))

	## shape
	# Return the shape of the mesh
	@property
	def shape(self):
		return self.meshes[0].shape

	## slice
	# Slice each mesh according to a given set of slices
	#
	# Takes a set of slices for each dimension of the mesh and performs the appropriate subslicing for each dimension's grid and returns the subslices as a tuple
	# @param slices tuple of tuples corresponding to the start and end index wanted in each underlying dimension
	def slice(self,slices):
		if len(slices) < self.dim:
			raise ValueError("trying to slice a Mesh with inadqute dimensions provided")
		elif len(slices) > self.dim:
			raise ValueError("trying to slice a Mesh with too many dimensions provided")

		keys = tuple((slice(*slc) for slc in slices))

		return self.__getitem__(keys)

	## subslice
	# generate a new mesh object corresponding to the original mesh object sliced along the relevant slices
	#
	# @param slices tuple of tuples corresponding to the start and end index wanted in each underlying dimension
	def sub_slice(self,slices):
		new_mesh = Mesh(self.base_shape)
		new_mesh.meshes = self.slice(slices)

		return new_mesh