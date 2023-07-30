'''
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A.
There are m words belonging to word group B. For each  words, check whether the word has appeared in group B or not.
Print the indices of each occurrence of M in group A . If it does not appear, print -1 .

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions  and  in group A. The second word, 'c', does not appear in group A, so print .

Expected output:

1 3
-1
Input Format

The first line contains integers,  and  separated by a space.
The next  lines contains the words belonging to group .
The next  lines contains the words belonging to group .

Constraints
1 < n <= 10000
1 < m <=100



Output Format

Output  lines.
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

Sample Input

STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Sample Output

1 2 4
3 5
Explanation

'a' appeared 3 times in positions 1, 2 and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group , you would print -1 .

'''

from collections import defaultdict
d = defaultdict(list)

list1=[]
n, m = map(int,input().split())
for i in range(1, n+1):
    d[input()].append(str(i))

for i in range(m):
    b = input()
    if b in d: print(' '.join(d[b]))
    else: print(-1)
