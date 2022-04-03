'''
###
input given already
Sample input:
[8, 9, 2, 2, 3, 4, 5, 2]
correspondingOutput
Sample output:
[8, 9, 2, 3, 4, 5]

----------------------------------------------------------------------
Sample input:
[4, 4, 4, 4]

Sample output:
[4]

----------------------------------------------------------------------
'''

#take input here
import ast
mylist=ast.literal_eval(input())
d={}


#remove duplicates from the list
for x in mylist:
    if x in d:
        d[x]+=1
    else:
        d[x]=1
ans=[]
for x in d:
    ans.append(x)
#print the list without duplicates
print(ans)

