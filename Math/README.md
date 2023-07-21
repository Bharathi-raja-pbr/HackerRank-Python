# Math 


# complex numbers

    These are numbers of form a+ib
    a-> real part
    b-> imaginary part
    i-> imaginary unit

# complex numbers as input

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
      They will also accept any Python object that has either a __complex__() or a __float__() method: these methods are used to convert the object to a complex
      or floating-point number, respectively, and the function is then applied to the result of the conversion.


# cmath functions:
       cmath.phase(x)-returns the phase of complex number x

       cmath.phase(complex(-1.0, 0.0))
       3.1415926535897931

       Phase angle:
                  Counter clockwise angle measured from the positive x-axis to the line segment that joins x to the origin

        cmath.polar(x) - returns the pair (r,phase) i.e, complex number in form of polar coordinates

        cmath.rect(r,phi) - Return the complex number x with polar coordinates r and phi. Equivalent to r * (math.cos(phi) + math.sin(phi)*1j).

# abs()
         This tool returns the modulus (absolute value) of complex number .

            abs(complex(-1.0, 0.0))
            1.0

        
