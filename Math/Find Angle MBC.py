'''
Problem Statement

https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath as c
import math  as m
ab=int(input())
bc=int(input())
print(str(int(round(m.degrees(m.atan(ab/bc)))))+chr(176))

'''
solution reference:
https://tinyurl.com/35vx9y23

'''
