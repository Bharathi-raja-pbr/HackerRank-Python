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
