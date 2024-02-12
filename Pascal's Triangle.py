'''

Pascal's Triangle
Description
A pascal's triangle is a very interesting mathematical concept.
Each number here is a sum of the two numbers directly above it.
Following is an 8 level Pascal's triangle:
##
You can read about Pascal's triangle here.
Your task is to print an nth level of Pascal's triangle.
The input will contain an integer n.
The output will contain 1 line of the list of numbers representing the nth row of Pascal's triangle.

Sample Input:
6
Sample Output:

[1, 5, 10, 10, 5, 1]


'''

#input has been taken for you
from math import factorial
n=int(input())
ans=[]
for x in range(n):
    ans.append(factorial(n-1)//((factorial(x))*(factorial(n-x-1))))

print(ans)
    
    
    

    


