'''
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Input Format
The first line contains a, the second line contains , b and the third line contains c .

Constraints
1< a <10
1< b <10
2< m <1000


Sample Input

3
4
5
Sample Output

81
1

'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
b=int(input())
m=int(input())

print(pow(a,b))
print(pow(a,b,m))
