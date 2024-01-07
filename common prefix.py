'''
----------------------------------------------------------------------
#
Sample input:
###
upgradData
upGradScience
Sample output:
upgrad
'''

#input has been taken for you

string1=input().lower()
string2=input().lower()

#start writing your code to find largest common prefix here
ans=""
for x in range(len(string1)):
    if string1[x]==string2[x]:
        ans=ans+string2[x]
    else:
        break
    
print(ans if ans!="" else -1)
