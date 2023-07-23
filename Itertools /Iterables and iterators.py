'''
You are given a list of  N lowercase English letters. For a given integer K, you can select any K indices (assume -1based indexing)
with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: ''.

Input Format

The input consists of three lines. The first line contains the integer N , denoting the length of the list.
The next line consists of N space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.

Note: The answer must be correct up to 3 decimal places.

Constraints

1<N<=10
1<k<=N

All the letters in the list are lowercase English letters.

Sample Input

4 
a a c d
2
Sample Output

0.8333

Explanation

(a,a) (a,c) (a,d) (a,c) (a,d) (c,d)

5 combinations contain a 
5/6=8.333
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
count=0
length=0
n=int(input())
lis=input().split()
k=int(input())

for i in combinations(lis,k):
     if 'a' in i:
        count+=1
     length+=1
val=count/length
print(f"{val:.3f}")

