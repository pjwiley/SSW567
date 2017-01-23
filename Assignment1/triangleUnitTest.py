# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:18:24 2017

@author: pjwiley
"""

import unittest

import Triangle_main
import sys

class TestStringMethods(unittest.TestCase):

    def test_main(self): 
        self.assertFalse(Triangle_main.classifyTriangle(3.0,4.0,5.0))
        self.assertTrue(Triangle_main.validate_input(1.0,1.0,1.0))

    def test_validate_input(self):
        self.assertTrue(Triangle_main.validate_input(1,1,1))
        self.assertTrue(Triangle_main.validate_input(1.0,1.0,1.0))
        self.assertFalse(Triangle_main.validate_input("one",1.0,1.0))
        self.assertFalse(Triangle_main.validate_input(1.0,"one",1.0))
        self.assertFalse(Triangle_main.validate_input(1.0,1.0,"one"))
        self.assertTrue(Triangle_main.validate_input(1,1,1))
        self.assertTrue(Triangle_main.validate_input(1.0,1.0,1.0))
        self.assertFalse(Triangle_main.validate_input(-1.0,1.0,1.0))
        self.assertFalse(Triangle_main.validate_input(1.0,-1.0,1.0))
        self.assertFalse(Triangle_main.validate_input(1.0,1.0,-1.0))
        self.assertFalse(Triangle_main.validate_input(sys.float_info.max,sys.float_info.max,sys.float_info.max))
        self.assertFalse(Triangle_main.validate_input(sys.float_info.max+1,sys.float_info.max,sys.float_info.max))

            
    def test_validate_triangle(self):
        self.assertTrue(Triangle_main.validate_triangle(3,4,5))
        self.assertTrue(Triangle_main.validate_triangle(3.0001, 4.00001, 5.000001))
        self.assertTrue(Triangle_main.validate_triangle(3.01, 4.01, 5.01))
       # self.assertFalse(Triangle_main.validate_triangle(0.0000, 4.01, 5.01)) Control flow assumes valid inputs before valid triangle is called
        self.assertTrue(Triangle_main.validate_triangle(2000.000, 2000.01, 2000.01))
        self.assertTrue(Triangle_main.validate_triangle(3, 3, 4))
        self.assertTrue(Triangle_main.validate_triangle(3.5, 2.2, 5))
        #self.assertFalse(Triangle_main.validate_triangle(-3, 4.01, 5.01)) Control flow assumes valid inputs before valid tri
        self.assertTrue(Triangle_main.validate_triangle(0.01, 0.01, 0.01))
        self.assertTrue(Triangle_main.validate_triangle(300000000, 400000000, 500000000))

    def test_triangle_type(self):
        self.assertEquals("Equalateral",Triangle_main.triangle_type(1,1,1))
        self.assertEquals("Isoscoles",Triangle_main.triangle_type(1,1,3))
        self.assertEquals("Scalene",Triangle_main.triangle_type(3,4,6))
        self.assertEquals("Scalene, Right",Triangle_main.triangle_type(3,4,5))
        
        
            
    def test_is_right_triangle(self): 
        self.assertEquals(", Right",Triangle_main.is_right_triangle(3,4,5))
            
if __name__ == '__main__':
    unittest.main()
    
    
    