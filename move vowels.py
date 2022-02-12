'''
----------------------------------------------------------------------
Sample input:
programming

Sample output:
oaiprgrmmng

----------------------------------------------------------------------
Sample input:
You love Python!

Sample output:
ouoeoY lv Pythn!

----------------------------------------------------------------------
'''

# Read the input string

s = input()
v="aeiou"
ans_v=""
ans_c=""
for x in s:
    if x in v:
        ans_v=ans_v+x
    else:
        ans_c=ans_c+x
print(ans_v+ans_c)
