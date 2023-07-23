'''
You are given a string S. Suppose a character 'c' occurs consecutively k times in the string.
Replace these consecutive occurrences of the character '(c,k)' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string S.

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between 0 and 9.

0<len(s)<=10^4
Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
S=input()
for key,group in groupby(S):
    print(f'({len(list(group))}, {key})',end=' ')

