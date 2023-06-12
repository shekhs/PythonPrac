'''

Q:####
#
area under fib series---must try
Fibonacci Series
Description
###
Compute and display Fibonacci series upto n terms where n is a positive integer entered by the user.
You can go here to read about Fibonacci series.
Sample Input:
5
Sample Output:
0
1
1
2
3
###
###
'''
#####
n=int(input())
#write your code here
a = [0,1]
for x in range(2,n):
    a.append(a[-1]+a[-2])
if n==1:
    print(0)
elif n==2:
    print(0)
    print(1)
else:
    for x in a:
        print(x)
