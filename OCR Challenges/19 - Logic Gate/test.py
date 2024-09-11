# this script runs some basic unit tests to ensure that all the functions work as expected
# this wasn't part of the challenge but I thought it'd be a good oppourtinity to learn a little about unit testing

import unittest # import unit test module
from hard import NOT, AND, OR, NAND, NOR, XOR

class TestClass(unittest.TestCase): # create a testing class which inherits from unittest.TestCase
    # def init(self):
        # self.inputs_1 = [[0, 1]]
        # self.inputs_2 = [[0, 0],
        #             [0, 1],
        #             [1, 0],
        #             [1, 1]]
        # this doesn't work due to library. idk why 
    
    def test_NOT(self): # create a test function for NOT
        inputs = [[0, 1]] # the inputs (as per truth table)
        output = [1, 0] # the expected outputs
        
        # to test not
        for i, j in enumerate(inputs):  # check for each value in truth table if it gives expected output
            self.assertEqual(NOT(j[0]), output[i])
    
    def test_AND(self):
        inputs = [[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]]
        output = [0, 0, 0, 1]
        
        for i, j in enumerate(inputs):
            self.assertEqual(AND(j[0], j[1]), output[i])
            
    def test_OR(self):
        inputs = [[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]]
        output = [0, 1, 1, 1]
        
        for i, j in enumerate(inputs):
            self.assertEqual(OR(j[0], j[1]), output[i])
            
    def test_NAND(self):
        inputs = [[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]]
        output = [1, 1, 1, 0]
        
        for i, j in enumerate(inputs):
            self.assertEqual(NAND(j[0], j[1]), output[i])
            
    def test_NOR(self):
        inputs = [[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]]
        output = [1, 0, 0, 0]
        
        for i, j in enumerate(inputs):
            self.assertEqual(NOR(j[0], j[1]), output[i])
            
    def test_XOR(self):
        inputs = [[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]]
        output = [0, 1, 1, 0]
        
        for i, j in enumerate(inputs):
            self.assertEqual(XOR(j[0], j[1]), output[i])
                
if __name__ == "__main__":
    unittest.main()
            
    
    