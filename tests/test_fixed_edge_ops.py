from unittest import TestCase
from src import fixed_edge_ops

class TestFixedEdgeOps(TestCase):

    def test_set_name(self):
        edge_op = fixed_edge_ops.FixedEdgeOps((1,2,3),(1,2,3))
        self.assertEqual(edge_op.name, 'fixed')
