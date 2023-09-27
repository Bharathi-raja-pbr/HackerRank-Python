
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
