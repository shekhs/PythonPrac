'''
Vote for Food
Description
Your team is going for camping and you are taking a vote to decide what food to pack for dinner.
Everyone gets a vote and the food item that gets at least one more than half of the votes wins. None of the items wins if nothing gets at least one more than half votes. Assume that every person gets only one vote.
The input will contain a list of food items where each occurrence of an item represents one vote. You should print the winning food item as output. If there is no clear winner, print "NOTA". 
##
Sample Input:
["pasta","pasta","pasta","pasta","pasta","paratha","paratha","paratha"]
Sample Output:
pasta

This question was asked in a Data Analyst interview.
'''

import ast,sys
input_str = sys.stdin.read()
votes = ast.literal_eval(input_str)
tgt = len(votes)//2 + 1
d={}
for x in votes:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
ans="NOTA"
for k,v in d.items():
    if v>=tgt:
        ans=k
print(ans)
