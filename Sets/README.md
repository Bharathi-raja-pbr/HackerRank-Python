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
        
        myset.discard(10)
        myset
        {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
        myset.remove(13)
        myset
        {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}


# COMMON SET OPERATIONS Using union(), intersection() ,difference() and symmetric_difference() functions.

        a = {2, 4, 5, 9}
        b = {2, 4, 11, 12}
        a.union(b) # Values which exist in a or b
        {2, 4, 5, 9, 11, 12}
        a.intersection(b) # Values which exist in a and b
        {2, 4}
        a.difference(b) # Values which exist in a but not in b
        {9, 5}
        a.symmetric_difference(b) # Values which exist in a and b but not in both
        {5,9,11,12}

         The union() and intersection() functions are symmetric methods:

        a.union(b) == b.union(a)
        True
        a.intersection(b) == b.intersection(a)
        True
        a.difference(b) == b.difference(a)
        False
  # Mutations

          .update() or |=
        Update the set by adding elements from an iterable/another set.
        
         H = set("Hacker")
         R = set("Rank")
         H.update(R)
         print H
        set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
        .intersection_update() or &=
        Update the set by keeping only the elements found in it and an iterable/another set.
        
         H = set("Hacker")
         R = set("Rank")
         H.intersection_update(R)
         print H
        set(['a', 'k'])
        .difference_update() or -=
        Update the set by removing elements found in an iterable/another set.
        
         H = set("Hacker")
         R = set("Rank")
         H.difference_update(R)
         print H
        set(['c', 'e', 'H', 'r'])
        .symmetric_difference_update() or ^=
        Update the set by only keeping the elements found in either set, but not in both.
        
         H = set("Hacker")
         R = set("Rank")
         H.symmetric_difference_update(R)
         print H
        set(['c', 'e', 'H', 'n', 'r', 'R'])
