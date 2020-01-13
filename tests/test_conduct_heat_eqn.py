from src import conduct_heat_eqn as heat_eqn
from unittest import TestCase

class TestConductHeatEqn(TestCase):

    def test_RHSAssert(self):
        problem = heat_eqn.ConductHeatEqn(alpha=0.005)
        self.assertRaises(AssertError, problem.RHS([[1,2],[3,4]]))
