'''
Sample input:

$yrr$ssrsr



Sample output:

True





Sample input:

$yrr$ssrsr%



Sample output:

False



Sample input:

ab#ab#aba



Sample output:

False



Sample input:

ab#ab#ab6a



Sample output:

True


'''


s="ab#ab#ab6a"
ans=[]
d={}
for x in s:
    if x in d:
        d[x]+=1
    else:
        d[x]=1

c=True
for x in d:
    ans.append(d[x])
ans.sort()
for x in range(len(ans)):
    if ans[x]!=x+1:
        c=False

print(c)
