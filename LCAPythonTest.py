from LCAPython import *  
  
import unittest

class test_LCA(unittest.testcase):
    def test_lowestCommonAncestor(self) : 
        self.assertEqual(ob1.lowestCommonAncestor(tree, 5, 1), 3)
    