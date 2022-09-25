#input data
####
m,n = input().split(",")
m=int(m)
n=int(n)
####
#start writing code here
a=[[0 for _ in range(n)] for _ in range(m)]
for x in range(m):
    for y in range(n):
        if x in [0,m-1] or y in [0,n-1]:
            a[x][y]=1

for x in a:
    print(x)
