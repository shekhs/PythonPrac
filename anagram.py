'''
----------------------------------------------------------------------
Sample input:
thing
night

Sample output:
True

Sample input:
upgrad
found

Sample output:
False
'''

#take input here
s1=[x for x in input()]
s2=[x for x in input()]
s1=sorted(s1)
s2=sorted(s2)
if s1==s2:
    print(True)
else:
    print(False)
#


#code here to check if they are anagrams or no


