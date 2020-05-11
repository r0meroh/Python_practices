# this is a file meant to be used as a 'module' within other python programs



import math # importing math to use the pi functionality
'''
    These three functions are to be use to calculate the area of an object.
    The three functions and their parameters are:
        def triangle:
            takes in a 'base' numeric value and a 'height' numeric value
            returns the base * height divided by 2
        def rectangle:
            takes in a 'width' numeric value and multiplies it by the 'height'
            numeric value
        def circle:
            takes in a 'radius' numeric value and multiplies it by pi
'''



def triangle(base , height): # function to calculate the area of a triangle
    return (base * height)/2

def rectangle(width , height): # function to calculate the area of a rectangle
    return width * height

def circle(radius): # function to calculate the area of a circle
    return  (radius**2) * math.pi


