'''
Problem statement
Clean Numbers
Description
While extracting data from different sources, often numeric values come in string format and with commas like 1,000 or 23,321 and also sometimes with spaces in start and beginning of the string. For simplicity, we will consider only integer values imbedded with commas. You will take the input and print the cleaned integer without commas and spaces.
###
----------------------------------------------------------------------
Input:
One line input of string, it will consist of only spaces commas and digits
###
Output:
Cleaned number
#
----------------------------------------------------------------------
Sample input:
         3,213

Sample output:
3213
###
----------------------------------------------------------------------
Sample input:
4,68,72,352          

Sample output:
46872352

----------------------------------------------------------------------
Note: Spaces will be either in the start or at the end.
'''

#input has been take  for you
value=input()

#start writing your code from here
ans=""
nums = "0123456789"
for x in value:
    if x in nums:
        ans=ans+x
print(ans)



