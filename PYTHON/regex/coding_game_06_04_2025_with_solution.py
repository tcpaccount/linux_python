'''
Extra characters are scattered in the sentences, among them: ' ? ! / , . : ) %
Your task is to count how many such characters are in a sentence.

! Space is not extra character !
Input
One sentence
Output
One number - quantity of extra characters
Constraints
3 <= lengh of sentence <= 100
Example
Input
Where's your motivation?
Output
2

----------------------
Example
???!!!///)))

Output
12

----------------------
Example
What are you looking for

Output
0

----------------------
Example
Hey, how are you doin'?:) Good luck, buddy!

Output
7
----------------------
'''

# My solution

import re


sentence = input()
# traight forward solution
#garbage = "' ? ! / , . : ) %".split()
#counter  = 0
#
#for i in sentence:
#    if i in garbage:
#        counter += 1
#print(counter)

# short regex solution
patter = r"['?!/,.:)%]"
print(len(re.findall(patter,sentence)))
