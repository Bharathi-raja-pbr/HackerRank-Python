'''
There is an array of  integers. There are also  disjoint sets, A and B , each containing  integers.
You like all the integers in set A and dislike all the integers in set B . Your initial happiness is  0.
For each  integer in the array, if i in A, you add 1 to your happiness. If i in B , you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints
1<n,m<=10^5

Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
queries=input().split()
A=set(input().split())
B=set(input().split())
score=sum([(x in A)-(x in B) for x in queries])
print(score)
