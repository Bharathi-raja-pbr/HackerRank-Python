'''
You are given a function f(x)=x^2 . You are also given K lists. The ith list consists of Ni elements.

You have to pick one element from each list so that the value from the equation below is maximized:

s= (f(x1)+f(x2)....+f(xi))%M

xi denotes the element picked from the ith list . Find the maximized value smax obtained.

 % denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. 
You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains 2 space separated integers k and m.
The next k lines each contains an integer n, denoting the number of elements in the  list,
followed by n space separated integers denoting the elements in the list.

Constraints
1<k<=7
1<M<=1000
1<Ni<=7

Output Format

Output a single integer denoting the value smax .

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 
Sample Output
5^2 + 9^2+ 10^2 = 25+81+100 =206
smax=206%1000 =206
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

k,m = map(int,input().split())
L = [list(map(int, input().split()))[1:] for i in range(k)]

result = 0
for i in itertools.product(*L):
    r = 0
    for n in i:
        r += n**2
        
    if result < r % m:
        result = r % m
print(result)
