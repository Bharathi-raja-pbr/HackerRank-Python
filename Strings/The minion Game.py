'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,S .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string S .
Note: The string S will contain only uppercase letters:A-Z .

Constraints

0<len(s)<10^6

Sample Input

BANANA
Sample Output

Stuart 12
'''

def minion_game(string):
    s=len(string)
    vowel = 0
    consonant = 0
     
    for i in range(s):
        if string[i] in 'AEIOU':
           vowel+=(s-i)
        else:
           consonant+=(s-i)
                
    if vowel < consonant:
        print('Stuart ' + str(consonant))
    elif vowel > consonant:
        print('Kevin ' + str(vowel))
    else:
        print('Draw')        

if __name__ == '__main__':
    s = input()
    minion_game(s)


'''
solution:
In the for loop, if character at index i of string is a vowel then we increment vowel by (s-i), else if string at index i is not a vowel 
then we increment consonant by (s-i).

for i in range(s):
        if string[i] in 'AEIOU':
           vowel+=(s-i)
        else:
           consonant+=(s-i)
To further understand above for loop let’s look at an example, if string = ‘BANANA’.

When i = 0, character at string[i] is a consonant (as ‘BANANA’[0] = ‘B’) and we increment consonant by (s-i) 
which equals to 6 as here s = 6 and i = 0, We do this because starting from ‘B’ there are six possible words (or substrings) that can be formed. 
[‘B’, ‘BA’, ‘BAN’, ‘BANA’, ‘BANAN’, ‘BANANA’].
On subsequent iterations when string[i] is a consonant at indices 2 and 4, we add additional substrings or the same substrings with additional instances.

'''
