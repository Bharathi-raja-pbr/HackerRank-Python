# Math 

# Math module
           Math has many built-in modules for trignometry,rounding off and other math operations.
            to import math module 
            import math

            to import all functions
            from math import *
# Math module functions:

# Power and Sqrt of a number:

                pow(base,exponent)
                pow(10,2)--> 100

                math.sqrt(100) --> 10

# Ceil and Floor:

                 math.ceil(x)  - returns the smallest integer >= x.
                 math.floor(x) - returns the largest integer <= x

              
                 
# Trignometry Math functions:

# Normal functions: returns ans in radians
                ->math.cos()
                ->math.sin()
                ->math.tan()

# Inverse functions :

                ->math.acos()
                ->math.asin()
                ->math.atan()

# Hyperbolic functions: eg sinh(),cosh()

                ->math.sinh()
                ->math.cosh()
                ->math.tanh()

# Inverse Hyperbolic functions: 

                ->math.asinh()
                ->math.acosh()
                ->math.atanh()

# Degrees and radians

           math.degrees(x)-> Convert angle x from radians to degrees
           math.radians(x) ->Convert angle x from degrees to radians 

# Complex numbers

    These are numbers of form a+ib
    a-> real part
    b-> imaginary part
    i-> imaginary unit

# Complex numbers as input

      n=complex(input())
      print(n)

      o/p: (3+2i)

# Polar coordinates
       A polar coordinate (r,phi)  is completely determined by modulus of x and phase angle .
      
      If we convert complex number x to its polar coordinate, we find:
      r : Distance from x to origin, i.e., sqrt(x^2+y^2)
      phi : Counter clockwise angle measured from the positive x-axis to the line segment that joins x to the origin.

 
# cmath — Mathematical functions for complex numbers
          This module is always available. It provides access to mathematical functions for complex numbers. 
      The functions in this module accept integers, floating-point numbers or complex numbers as arguments.
      They will also accept any Python object that has either a __complex__() or a __float__() method:
      these methods are used to convert the object to a complex or floating-point number, respectively, 
      and the function is then applied to the result of the conversion.


# cmath functions:

# phase()
       cmath.phase(x)-returns the phase of complex number x

       cmath.phase(complex(-1.0, 0.0))
       3.1415926535897931

       Phase angle:
                  Counter clockwise angle measured from the positive x-axis to the line segment that joins x to the origin
# polar()
        cmath.polar(x) - returns the pair (r,phase) i.e, complex number in form of polar coordinates
# rect()
        cmath.rect(r,phi) - Return the complex number x with polar coordinates r and phi.
        Equivalent to r * (math.cos(phi) + math.sin(phi)*1j).

# abs()
         This tool returns the modulus (absolute value) of complex number .

            abs(complex(-1.0, 0.0))
            1.0
