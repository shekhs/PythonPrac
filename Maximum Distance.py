'''

Maximum Distance
Description
You will be given a list of repeated elements. You have to find the maximum distance between two same elements. The answer will be zero if there are no repeated elements.
----------------------------------------------------------------------
#####
Input:
A non-empty list of integers.
Output:
A single integer denoting the maximum distance between two same integers.
#########
----------------------------------------------------------------------
Sample input:
[1, 2, 3, 2, 5, 1, 2, 4, 6, 2, 7, 8, 6]
####
Sample output:
8

Explanation:
Max distance for 1: 5
Max distance for 2: 8
Max distance for 3: 0
Max distance for 4: 0
Max distance for 5: 0
Max distance for 6: 4
Max distance for 7: 0
Max distance for 8: 0
'''

#input has been taken for you
import ast
input_list= ast.literal_eval(input())
d={}
for x in range(len(input_list)):
    if input_list[x] in d:
        d[input_list[x]].append(x)
    else:
        d[input_list[x]]=[x]
ans=[]
for x in d:
    ans.append(d[x][-1]-d[x][0])
print(max(ans))
        
#start writing your code from here
