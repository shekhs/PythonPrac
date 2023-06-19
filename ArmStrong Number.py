'''#
Armstrong number
Description
##
Any number, say n is called an Armstrong number if it is equal to the sum of its digits, where each is raised to the power of number of digits in n.


For example:
153=13+53+33
Write Python code to determine whether an entered three digit number is an Armstrong number or not. 
Assume that the number entered will strictly be a three digit number.
Print "True" if it is an Armstrong number and print "False" if it is not.
###
Sample Input:
153
##
###
Sample Output:
True
###
'''
n=int(input())
s=str(n)
sm = 0
for x in s:
    sm = sm+(int(x)**(len(s)))
if sm == n:
    print(True)
else:
    print(False)

