'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.

Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

if __name__ == '__main__':
    N = int(input())
    lis=[]
    for i in range(N):
        query=input()
        q=query.split(' ')
        cmd =q[0]
        if q[0]=='insert':
            lis.insert(int(q[1]),int(q[2]))
            #print(lis)
        elif q[0]=='print':
            print(lis)
        elif q[0]=='append':
            lis.append(int(q[1]))
        elif q[0]=='sort':
            lis.sort()
        elif q[0]=='pop':
            lis.pop()
        elif q[0]=='reverse':
            lis.reverse()
        elif q[0]=='remove':
            lis.remove(int(q[1]))
            
        

        
        
