#take input of the number here
n=int(input())
######
rev=0
#write code to reverse the number here
while(n>0):
    rem = n%10
    n=n//10
    rev=rev*10+rem
print(rev)


