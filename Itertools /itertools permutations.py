'''
You are given a string S.
Your task is to print all possible permutations of size K of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string S and the integer value K.

Constraints
0<K<=len(S)

The string contains only UPPERCASE characters.

Output Format

Print the permutations of the string S on separate lines.

Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
Explanation

All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S,k=input().split()
a=list(permutations(S,int(k)))
for i in sorted(a):
    print(''.join(i))
