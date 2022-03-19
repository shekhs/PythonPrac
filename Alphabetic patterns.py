'''
###
###
Description
#
Given a positive integer 'n' less than or equal to 26, you are required to print the below pattern 
####
###
###
Sample Input: 5 
 
Sample Output : 
--------e-------- 
------e-d-e------ 
----e-d-c-d-e---- 
--e-d-c-b-c-d-e-- 
e-d-c-b-a-b-c-d-e 
--e-d-c-b-c-d-e-- 
----e-d-c-d-e---- 
------e-d-e------ 
--------e-------- 
 
Sample Input  : 3 
 
Sample Output : 
----c---- 
--c-b-c-- 
c-b-a-b-c 
--c-b-c-- 
----c----

Please note that this question was asked in a Data Scientist interview.

'''


n = int(input())
stt = "abcdefghijklmnopqrstuvwxyz"
lines = (n-1)*2 + 1
cols=2*lines-1

def makePatt(n,i):
    s = ("-".join(stt[i:n]))
    ss = s[1:]
    ss=ss[::-1]
    mid_s = ss+s
    return mid_s

for x in range(lines):
    if x<n:
        i=n-x-1
    else:
        i=x-n+1
    st = makePatt(n,i)
    mpy = (cols-len(st))//2
    print("-"*mpy+st+"-"*mpy) 

#print(makePatt(5,3))


