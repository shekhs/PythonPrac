'''
INT or STR
'''

in_str=input()

#find out if in_str is integer or not
nums = "0123456789 "
s="INT"
if in_str[0]=="-":
    in_str=in_str[1:]
for x in in_str:
    if x not in nums:
        s="STR"
        break
print(s)
