'''
PS

Lego Stack
##
Description
You are given a row of Lego Blocks consisting of n blocks. All the blocks given have a square base whose side length is known. You need to stack the blocks over each other and create a vertical tower. Block-1 can go over Block-2 only if sideLength(Block-2)=>sideLength(Block-1).
#
From the row of Lego blocks, you can only pick up either the leftmost or rightmost block.

Print "Possible" if it is possible to stack all n cubes this way or else print "Impossible".
#
Input Format:

The input will contain a list of n integers representing the side length of each block's base in the row starting from the leftmost.


Sample Input:
###
[5 ,4, 2, 1, 4 ,5]

Sample Output:
#####
Possible
'''

import ast,sys
input_str = sys.stdin.read()
sides = ast.literal_eval(input_str)#list of side lengths
c=True

while(len(sides)>0):
    if sides[0]>sides[-1]:
        side=sides[0]
        sides=sides[1:]
    else:
        side=sides[-1]
        sides=sides[:-1]
    if len(sides)==0:
        break
    if side<sides[0] or side<sides[-1]:
        c=False
        break
    
if c:
    print("Possible")
else:
    print("Impossible")
    
###
