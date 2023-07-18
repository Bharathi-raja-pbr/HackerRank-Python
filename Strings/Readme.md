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

  isalnum()-checks whether the string is alphanumerical or not
  isalpha()-checks whether the string contains only alphabets
  isdigit()-checks whether the string contains only numbers
  islower()-checks whether the string contains only lowercase letters
  isupper()-checks whether the string contains only uppercase letters
  toupper()-converts the entire string to uppercase
  tolower()-converts the entire string to lowercase
  casefold()-converts every uppercase to lowercase
  capitalize()-converts the first letter to uppercase
  count(sub,start,stop)-counts the occurence of subtring in string 
  Swapcase()-alters the cases of the string
  title()-converts the first letter of each word in string to uppercase

  other functions: isnumeric(),isacii()

  # 
     
