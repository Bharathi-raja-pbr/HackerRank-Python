'''
Given  sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format

The first line of input contains an integer,M .
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output

5
9
11
12
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
set1=map(int,input().split())
N=int(input())
set2=map(int,input().split())


set1=set(set1)
set2=set(set2)
result=list(set1.union(set2) - set1.intersection(set2))
result.sort()
for i in result:
    print(i)
