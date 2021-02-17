# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author:Lingwen Kong
Documentation: HW02a
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertNotEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2,3,4 should be scalene')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2,2,3 should be isosceles')

    def testNonTriangles(self):
        self.assertEqual(classifyTriangle(10, 5, -2), 'InvalidInput', " 10, 5, -2 Invalid")

    def testBounds(self):
        self.assertEqual(classifyTriangle(201, 201, 201), "InvalidInput", "201, 201, 201 out of bounds")

    def testType(self):
        self.assertEqual(classifyTriangle(201.55, 201.55, 201), "InvalidInput", "201.55, 201.55, 201 type")


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
