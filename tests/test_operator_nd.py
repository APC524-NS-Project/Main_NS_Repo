from unittest import TestCase
from src import operator_nd

class TestOperatorND(TestCase):

    def test_tuple_arg(self):
        self.assertRaises(AssertionError, operator_nd.OperatorND, 
                            [1,2,3,4,5])

    def test_arg_length(self):
        self.assertRaises(AssertionError, operator_nd.OperatorND)
