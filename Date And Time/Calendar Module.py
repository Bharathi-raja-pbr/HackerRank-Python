'''
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

Constraints
2000<year<3000

Output Format

Output the correct day in capital letters.

Sample Input

08 05 2015
Sample Output

WEDNESDAY
Explanation

The day on August 5th 2015 was WEDNESDAY.

'''

import calendar
x,y,z=map(int,input().split())
n=calendar.weekday(z,x,y)

if n==0:
    print("MONDAY")
elif n==1:
    print("TUESDAY")
elif n==2:
    print("WEDNESDAY")
elif n==3:
    print("THURSDAY")
elif n==4:
    print("FRIDAY")
elif n==5:
    print("SATURDAY")
else:
    print("SUNDAY")
