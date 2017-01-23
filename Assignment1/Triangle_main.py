# -*- coding: utf-8 -*-

import sys
from math import sqrt

def classifyTriangle(a: float, b: float, c: float):
    if validate_input(a,b,c)==0: #if invalid input, exit
        return "0"
    if (validate_triangle(a,b,c)==0): #if invalid triangle, exit
        return
    print(triangle_type(a, b, c)) # Valid inputs, and is a triangle - Print it!
    return

if __name__ == '__main__':
    classifyTriangle(a,b,c)

TOLERANCE = .001    
    
def validate_input(a,b,c):
    maxInput = ((sqrt(sys.float_info.max) / 2.0) - 1.0);
    try:
        side1=(float(a))
        side2=(float(b))
        side3=(float(c))
        return ((side1 > TOLERANCE and side1 < maxInput) and
                (side2 > TOLERANCE and side2 < maxInput) and
                (side3 > TOLERANCE and side3 < maxInput))
    except:
        print("Inputs must be numbers.")
        return False

def validate_triangle(a,b,c):
    return  (abs(a + b - c) > TOLERANCE) and (abs(a + c - b) > TOLERANCE) and (abs(b + c - a) > TOLERANCE)
    

def triangle_type(a,b,c):
    try:
        triangleType = "unknown"
        if abs(a - b) < TOLERANCE and abs(b - c) < TOLERANCE and abs(a - c) < TOLERANCE:
            triangleType="Equalateral"
        elif (abs(a - b) < TOLERANCE) or (abs(a - c) < TOLERANCE) or (abs(b - c) < TOLERANCE):
            triangleType="Isoscoles" + is_right_triangle(a,b,c)
        else:
            triangleType= "Scalene" + is_right_triangle(a,b,c)
        return triangleType
    except:
        print("Unknown triangle determination error in type block") # pjw: is this needed?

def is_right_triangle(a,b,c):
    a2 = a*a;
    b2 = b*b;
    c2 = c*c;
    try:
        if ((abs(a2 + b2 - c2) < TOLERANCE) 
            or (abs(a2 + c2 - b2) < TOLERANCE) 
            or (abs(b2 + c2 - a2) < TOLERANCE)):
            return ", Right"
        else:
            return ""
    except:
        print("Unknown triangle angle calculations") # pjw is this needed? 