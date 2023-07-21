'''
You are given a string S.
Your task is to print all possible combinations with replacement, up to size K, of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value K separated by a space.

Constraints
0<k<=len(S)

The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string  on separate lines.

Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

S,K=input().split()
a=list(combinations_with_replacement(sorted(S),int(K)))
for i in a:
    print(''.join(i))
    
