s="HAnnah"
####
s=s.lower()
pal = 1
l=len(s)
for x in range(l):
    if s[x]!=s[l-x-1]:
        pal = 0
if pal:
    print(1)
else:
    print(0)
    
