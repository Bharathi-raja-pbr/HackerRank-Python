'''
You are given a two lists A and B. Your task is to compute their cartesian product X.

Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note: A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format

The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.

Both lists have no duplicate integer elements.

Constraints

0< len(A),len(B)<30

Output Format

Output the space separated tuples of the cartesian product.

Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a=list(map(int,input().split()))
b=list(map(int,input().split()))

x=list(product(a,b))
for i in x:
    if i==x[-1]:
        print(i)
    else:
        print(i,end=' ')
