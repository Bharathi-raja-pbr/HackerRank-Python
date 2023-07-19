
'''
Task
Students of District College have a subscription to English and French newspapers.
Some students have subscribed to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper.
Your task is to find the total number of students who have subscribed to only English newspapers.

Input Format

The first line contains an integer,n , the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains ,b the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.

Constraints
0< total no of students<1000

Output Format

Output the total number of students who have at least one subscription.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

4
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1=set(map(int,input().split()))
b=int(input())
set2=set(map(int,input().split()))
ans=set1.difference(set2)
print(len(ans))
