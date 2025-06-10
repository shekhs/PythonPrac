'''
Balanced Brackets
#
---------------------------------------------------------------------
Sample input:
){[[]]}())()
##
Sample output:
No

----------------------------------------------------------------------
Sample input 2:
[](){[]()(){}}

Sample output 2:
Yes
'''


#take input
inp=input()
a=[]
c=True
for x in inp:
    if x in ["(","{","["]:
        a.append(x)
    else:
        if len(a)>0:
            a.pop()
        else:
            c=False

if c and len(a)==0:
    print("Yes")
else:
    print("No")

