## @file gridoperator.py
#
# Based on a grid and an n-diemnsional scheme this class generates a corresponding grid operator
# The grid operator is a callable object that if given a gridqty that shares a gridspec the grid operator will return 
# a gridqty of the same size with the results of the given finite difference operator applied to the 
# initial gridqty
# Grid operator uses the interior and boundary nd operators in nd scheme along with a populator to generate 
# operator matricies for each dimension and then combines them to produce a single operator matrix

import numpy as np
import operatormatrix
import mesh
import populator

## GridOperator
# GridOperator class definition
class GridOperator():
	
	def __init__(self,spec,ndscheme):
