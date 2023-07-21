'''
You are given a string S.
Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.

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

A
C
H
K
AC
AH
AK
CH
CK
HK
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT


from itertools import combinations

S,K=input().split()
for i in range(1,int(K)+1):
    a=list(combinations(sorted(S),i))
    for i in a:
         print(''.join(i))
    
