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
