import unittest
import numpy as np
import src.grid as grid
import src.operatormatrix as operatormatrix

class testCartesianGridSpec(unittest.TestCase):
    def setUp(self):
        test_shape = ((-1,-.5,0,.5,1),(-2,0,2,4))
        self.tgrid = np.ones((5,4))
        self.tgrid[3,2]=12
        self.tgrid[1,1]=5
        self.gspec = grid.CartesianGridSpec(test_shape)
        
    def test_spacing(self):
        self.assertEqual(self.gspec.spacing[0], 0.5)
        self.assertEqual(self.gspec.spacing[1], 2)

class testGridScalar(unittest.TestCase):
    def setUp(self):
        test_shape = ((-1,-.5,0,.5,1),(-2,0,2,4))
        self.tgrid = np.ones((5,4))
        self.tgrid[3,2]=12
        self.tgrid[1,1]=5
        self.gspec = grid.CartesianGridSpec(test_shape)
        self.grid = grid.GridScalar(self.gspec,self.tgrid)

    def test_makegrid(self): #checks if grid was made correctly
        np.array_equal(self.tgrid,self.grid.grid)
        
    def test__getattr__(self):
        self.grid.shape #tries to use numpy attribute shape
        
    def test__add__(self):
        add_test1 = self.grid + self.grid
        add_test2 = self.grid + 0
        self.assertEqual(add_test1.grid[0,0],2)
        self.assertEqual(add_test2.grid[0,0],1)
        
    def test__mul__(self):
        mul_test1 = self.grid*self.grid
        mul_test2 = self.grid*5
        mul_test3 = 5*self.grid
        self.assertEqual(mul_test1.grid[0,0],1)
        self.assertEqual(mul_test2.grid[0,0],5)        
        self.assertEqual(mul_test3.grid[0,0],5)         

    def test_qtyshape(self):
        self.assertEqual(self.grid._qtyshape(),())    
        
    def test_getslice(self):
        indices = ((0,2),(1,3))
        idxs = [range(*t) for t in indices]
        
        np.array_equal(self.grid.getslice(indices),self.tgrid[np.ix_(*idxs)])
        
    def test_setslice(self):
        indices = ((0,2),(1,3))
        self.grid.setslice(indices,np.zeros(4))
        np.array_equal(self.grid.getslice(indices).all,0)        
    
    def test_applyOp(self):
        testspec = grid.CartesianGridSpec(((0,1,2),(0,1,2)))
        test_int = np.zeros((3,3))
        test_int[1,1] = 1
        testgrid = grid.GridScalar(testspec,test_int)

        x_out_cor = operatormatrix.OperatorMatrix(9)
        int_points = [1,4,7]
        weights = [1,-2,1]
        for pt in int_points:
            x_out_cor[pt,pt-1:pt+2] = weights

        left_points = [0,3,6]
        for pt in left_points:
            x_out_cor[pt,pt:pt+3] = weights

        right_points = [2,5,8]
        for pt in right_points:
            x_out_cor[pt,pt-2:pt+1] = weights

        y_out_cor = operatormatrix.OperatorMatrix(9)
        yweights = [1,0,0,-2,0,0,1]
        for j in range(3):
            for i in range(3):
                y_out_cor[3*i+j,j:j+7] = yweights

        laplace = y_out_cor + x_out_cor

        results = testgrid.applyOp(laplace)

        result_cor = np.zeros((3,3))
        result_cor[1,:] = [-2,-4,-2]
        result_cor[0,1] = -2
        result_cor[2,1] = -2

        np.testing.assert_array_equal(result_cor,results.grid)
        
if __name__ == '__main__':
    unittest.main()