
# HackerRank-Python
Welcome to my Git
This repository contains the solutions for the python preparation questions in HackerRank



# Collections
  
  This module implements specialized container datatypes providing alternatives to Python’s general purpose
  built-in containers, dict, list, set, and tuple.

# Collections.Counter()

    A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

    >>> from collections import Counter
    >>> 
    myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
    print Counter(myList)
    Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
    
    >>>
    print Counter(myList).items()
    [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
    
    >>> 
    print Counter(myList).keys()
    [1, 2, 3, 4, 5]
    
    >>> 
    print Counter(myList).values()
    [3, 4, 4, 2, 1]

  # collections.defaultdict()

              The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only 
            difference is that a defaultdict will have a default value if that key has not been set yet.If you didn't use a defaultdict you'd have to 
            check to see if that key exists, and if it doesn't, set it to what you want.
            
            For example:
            
            from collections import defaultdict
            d = defaultdict(list)
            d['python'].append("awesome")
            d['something-else'].append("not relevant")
            d['python'].append("language")
            for i in d.items():
                print i
            
            This prints:
            
            ('python', ['awesome', 'language'])
            ('something-else', ['not relevant'])

            Example 2:
            
            from collections import defaultdict
            def def_value():
                return "Not Present"
                  
            # Defining the dict
            d = defaultdict(def_value)
            d["a"] = 1
            d["b"] = 2
              
            print(d["a"])
            print(d["b"])
            print(d["c"])


# Calendar

      import calendar
      The calendar module allows you to output calendars and provides additional useful functions for them.

# calendar.setfirstweekday(weekday)
    Sets the weekday (0 is Monday, 6 is Sunday) to start each week.
    The values MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, and SUNDAY are provided for convenience.
    For example, to set the first weekday to Sunday:
    
    import calendar
    calendar.setfirstweekday(calendar.SUNDAY)

# calendar.firstweekday()
    Returns the current setting for the weekday to start each week.

# calendar.isleap(year)
    Returns True if year is a leap year, otherwise False.
  
    calendar.isleap(2020)
    -->True

# calendar.leapdays(y1, y2)
    Returns the number of leap years in the range from y1 to y2 (exclusive), where y1 and y2 are years.

         calendar.leapdays(2000,2024)
         ->6
         2000,2004,2008,2012,2016,2020

# calendar.weekday(year, month, day)
    Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).

# calendar.weekheader(n)
    Return a header containing abbreviated weekday names. n specifies the width in characters for one weekday.

    mon tue wed thu fri sat sun

# calendar.monthrange(year, month)
    Returns weekday of first day of the month and number of days in month, for the specified year and month.

# calendar.monthcalendar(year, month)
          Returns a matrix representing a month’s calendar.
          Each row represents a week; days outside of the month a represented by zeros.
          Each week begins with Monday unless set by setfirstweekday().


# Datetime

           import datetime

# Print current time
           x = datetime.datetime.now()
           print(x)

# The strftime() Method
            The datetime object has a method for formatting date objects into readable strings.
            The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

            x = datetime.datetime(2018, 6, 1)
            print(x.strftime("%B"))

            o/p-> June

            Directive	  Description	                                               Example
            %a	        Weekday, short version	                                    Wed	
            %A	        Weekday, full version	                                          Wednesday	
            %w	        Weekday as a number 0-6, 0 is Sunday	                        3	
            %d	        Day of month 01-31	                                          31	
            %b	        Month name, short version	                                    Dec	
            %B	        Month name, full version	                                    December	
            %m	        Month as a number 01-12	                                    12	
            %y	        Year, short version, without century	                        18	
            %Y	        Year, full version	                                          2018	
            %H	        Hour 00-23	                                                17	
            %I	        Hour 00-12	                                                05	
            %p	        AM/PM	                                                      PM	
            %M	        Minute 00-59	                                                41	
            %S	        Second 00-59	                                                08	
            %f	        Microsecond 000000-999999	                                    548513	
            %z	        UTC offset	                                                +0100	
            %Z	        Timezone	                                                      CST	
            %j	        Day number of year 001-366	                                    365	
            %U	        Week number of year, Sunday as the first day of week, 00-53	52	
            %W	        Week number of year, Monday as the first day of week, 00-53	52	
            %c	        Local version of date and time	                              Mon Dec 31 17:41:00 2018	
            %C	        Century	                                                      20	
            %x	        Local version of date	12/31/18	
            %X	        Local version of time	17:41:00	
            %%	        A % character	                                                %	
            %G	        ISO 8601 year	                                                2018	
            %u	        ISO 8601 weekday (1-7)	                                    1	
            %V	        ISO 8601 weeknumber (01-53)

# Strptime() method
            strptime() is another method available in DateTime which is used to format the time stamp which is in string format to date-time object.

            Syntax: datetime.strptime(time_data, format_data)


# Itertools 

      This module implements a number of iterator building blocks
      The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.
      Together, they form an “iterator algebra” making it possible to construct specialized tools succinctly and efficiently in pure Python.

# itertools.product()

      This tool computes the cartesian product of input iterables.
      It is equivalent to nested for-loops.
      For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
      
      Sample Code
      
      from itertools import product
      >>>
      print list(product([1,2,3],repeat = 2))
      [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
      >>>
      print list(product([1,2,3],[3,4]))
      [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
      >>>
      A = [[1,2,3],[3,4,5]]
      print list(product(*A))
      [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]

# itertools.permutations(iterable,r)

      This tool returns successive  length permutations of elements in an iterable.
      If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.
      Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted,
      the permutation tuples will be produced in a sorted order.
      
      Sample Code
      
      from itertools import permutations
      
      print list(permutations(['1','2','3']))
      [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
      >>> 
      print list(permutations(['1','2','3'],2))
      [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
      >>>
      print list(permutations('abc',3))
      [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

# itertools.combinations(iterable,r)

      >>> from itertools import combinations
      >>> 
      print list(combinations('12345',2))
      [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
      >>> 
      A = [1,1,3,3,3]
      print list(combinations(A,4))
      [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

      A=Hack
      combinations --> A C H K AC AH AK CH CK HK

# itertools.combinations_with_replacement(iterable,r)

      from itertools import combinations_with_replacement
      >>> 
      print list(combinations_with_replacement('12345',2))
      [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'),
      ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
      >>> 
      A = [1,1,3,3,3]
      print list(combinations(A,2))
      [(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]


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

                pow(base,exponent,mod) -> computes a^b mod m ,if m present b cannot be negative

                pow(3,4,5) -> 1

                math.sqrt(100) --> 10

# Ceil and Floor:

                 math.ceil(x)  - returns the smallest integer >= x.
                 math.floor(x) - returns the largest integer <= x

# Divmod:
                
                 One of the built-in functions of Python is divmod, which takes two arguments a and  b 
                 and returns a tuple containing the quotient of a/b first and then the remainder . No need to use math module

                 For example:

                  print divmod(177,10)
                  (17, 7)
                  Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

                 
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

# Link for Reference
           https://docs.python.org/2/library/cmath.html

# SETS

# Introduction
  A set is an unordered collection of elements without duplicate entries.
  When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
  Basically, sets are used for membership testing and eliminating duplicate entries.

        print set()
        set([])
        
        print set('HackerRank')
        set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
        
        print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
        set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])
        
        print set((1,2,3,4,5,5))
        set([1, 2, 3, 4, 5])
        
        print set(set(['H','a','c','k','e','r','r','a','n','k']))
        set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])
        
        print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
        set(['Hacker', 'Rank'])
        
        print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
        set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])

        Sets are an unordered collection of unique values. A single set contains values of any immutable data type.

# CREATING SETS

        myset = {1, 2} # Directly assigning values to a set
        myset = set()  # Initializing a set
        myset = set(['a', 'b']) # Creating a set from a list
        myset
        {'a', 'b'}


# MODIFYING SETS

  # Using the add() function:
        
        myset.add('c')
        myset
        {'a', 'c', 'b'}
        myset.add('a') # As 'a' already exists in the set, nothing happens
        myset.add((5, 4))
        myset
        {'a', 'c', 'b', (5, 4)}

  # Using the update() function:
        
        myset.update([1, 2, 3, 4]) # update() only works for iterable objects
        myset
        {'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
        myset.update({1, 7, 8})
        myset
        {'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
        myset.update({1, 6}, [5, 13])
        myset
        {'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}

# REMOVING ITEMS

        Both the discard() and remove() functions take a single value as an argument and removes that value from the set.
        If that value is not present, discard() does nothing, but remove() will raise a KeyError exception.
# discard() 
        myset.discard(10)
        myset
        {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
# remove()
        myset.remove(13)
        myset
        {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}

# pop()
       removes the lastelement by default.
       It removes and returns the argument

       a={1,2,3}
       b=a.pop()
       print(b)

       o/p:
       3

# COMMON SET OPERATIONS Using union(), intersection() ,difference() and symmetric_difference() functions.

        a = {2, 4, 5, 9}
        b = {2, 4, 11, 12}
# a.union(b) # Values which exist in a or b
        {2, 4, 5, 9, 11, 12}
# a.intersection(b) # Values which exist in a and b
        {2, 4}
# a.difference(b) # Values which exist in a but not in b
        {9, 5}
# a.symmetric_difference(b) # Values which exist in a and b but not in both
        {5,9,11,12}

         The union() and intersection() functions are symmetric methods:

        a.union(b) == b.union(a)
        True
        a.intersection(b) == b.intersection(a)
        True
        a.difference(b) == b.difference(a)
        False
  # Mutations

  # .update() or |=
        Update the set by adding elements from an iterable/another set.
        
         H = set("Hacker")
         R = set("Rank")
         H.update(R)
         print H
        set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
        
  # .intersection_update() or &=
        Update the set by keeping only the elements found in it and an iterable/another set.
        
         H = set("Hacker")
         R = set("Rank")
         H.intersection_update(R)
         print H
        set(['a', 'k'])
        
  # .difference_update() or -=
        Update the set by removing elements found in an iterable/another set.
        
         H = set("Hacker")
         R = set("Rank")
         H.difference_update(R)
         print H
        set(['c', 'e', 'H', 'r'])
        
  # .symmetric_difference_update() or ^=
        Update the set by only keeping the elements found in either set, but not in both.
        
         H = set("Hacker")
         R = set("Rank")
         H.symmetric_difference_update(R)
         print H
        set(['c', 'e', 'H', 'n', 'r', 'R'])
# issuperset():
        Returns true if A is a superset of B,else false
# issubset():
        Returns true if A is a subset of B,else false
# isdisjoint():
        Returns true if A is a disjoint set of B,else false


# Python Strings

# Definition:
    Strings are words surrounded by quotes.Strings can be traversed.Strings can be sliced.
    
# Declaration:
     -> s=''
     -> s=""

# Get as i/p from user:
    str=input()

# Traversal:

    for x in str:
        print(str)

# Indexing:

     str='apple'
     str[0]='a'
     str[-1]='e'

# Slicing:
     str[start:stop:step]
     str[0:] -> prints entire string
     str[:5] -> prints string starting from index 0 to 4
     str[1:5] -> prints string from index 1 to 4


# String Reverse:
      str[::-1] -> reverses the entire string

# Split and Join:
      split:
           It splits the string based on the delimiter

            str='this is github'
            a=str.split(' ') #splits removing spaces instead of space any delimiter can be provided
            o/p: ['this','is','github']
      join:
           It joins array of strings
           a=['this','is','github']
           str='-'.join(a)
           o/p: this-is-github
           
# Built-in string functions:

      isalnum()-checks whether the string is alphanumerical or not.
      isalpha()-checks whether the string contains only alphabets.
      isdigit()-checks whether the string contains only numbers.
      islower()-checks whether the string contains only lowercase letters.
      isupper()-checks whether the string contains only uppercase letters.
      toupper()-converts the entire string to uppercase.
      tolower()-converts the entire string to lowercase.
      casefold()-converts every uppercase to lowercase.
      capitalize()-converts the first letter to uppercase.
      count(sub,start,stop)-counts the occurence of subtring in string. 
      Swapcase()-alters the cases of the string.
      title()-converts the first letter of each word in string to uppercase.
    
      other functions: isnumeric(),isacii().

  #   Alignment:
        s='apple'
        ljust():
            left aligns the string
            ->s.ljust(2)
                apple**
        rjust():
             right aligns the string
             ->s.rjust()
                 **apple
        center():
              aligns string to center
              ->s.center()
                *apple*
 # Textwrap:
         Textwrap is a module ,which needs to be imported in order to access its function.

         import textwrap

         function:
          ->fill()-it creates a rectangular box
               fill(string,maxwidth):
               s='ABCDEFGH'
               textwrap.fill(s,3)
               o/p: 
               ABC
               DEF
               GH
          
          ->wrap() - it traverses the string in such way that its splitted and stored in single line
                wrap(string,width)
                s='ABCDEFGH'
                textwrap.wrap(s,3)
                o/p:
                ['ABC','DEF','GH']

 # String module:
           String module has few useful functions

           import string

               ascii_lowercase: contains all lowercase letters in a string
                result=string.ascii_lowercase
                print(result)
                o/p: abcdefghijklmnopqrstuvxyz

               ascii_uppercase: contains all uppercase letters in a string
                result=string.ascii_uppercase
                print(result)
                o/p: ABCDEFGHIJKLMNOPQRSTUVWXYZ

# String Formatting
             In python strings can be formatted in such a way we need the output
             syntax: f'#statements' or f"statements"

             But why formatting,
             a=10
             b=20
             in order to print 10 is greater than 20 we use 
             -> print(str(a)+"is greater than"+str(b))
             this can be eliminated using formatting
             -> print(f"{a} is greater than {b}")

             example1:

             print decimal value with 2 positions after decimal point

             val=100/5
             print(f"{val:.2f}")

             example 2:
             To print binary,decimal,hexadecimal,octal values of a number

             num=20
             print(f"{num:b} {num:o} {num:X} {numm}")

             if width to be added
             i=20
             print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")
             


# Exceptions:

          Exceptions
          Errors detected during execution are called exceptions.
          
          Examples:
          
# ZeroDivisionError
          This error is raised when the second argument of a division or modulo operation is zero.
          
          >>> a = '1'
          >>> b = '0'
          >>> print int(a) / int(b)
          >>> ZeroDivisionError: integer division or modulo by zero
          
# ValueError
          This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
          
          >>> a = '1'
          >>> b = '#'
          >>> print int(a) / int(b)
          >>> ValueError: invalid literal for int() with base 10: '#'
          To learn more about different built-in exceptions click here.
          
# Handling Exceptions
          The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to 
          specify handlers for different exceptions.
          
          #Code
          try:
              print 1/0
          except ZeroDivisionError as e:
              print "Error Code:",e
