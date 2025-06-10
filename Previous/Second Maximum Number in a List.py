'''
Description
Given a list of numbers, find the second largest number in the list.

Note: There might be repeated numbers in the list. If there is only one number present in the list, return 'not present'.

Examples:
Input 1:
[7, 2, 0, 9, -1, 8]
Output 1:
8
###
Input 2:
[3, 1, 4, 4, 5, 5, 5, 0, 2, 2]
Output 2:
4

Input 2:
[6, 6, 6, 6, 6]
Output 2:
not present

'''
##
# Read the input list
import ast
input_str = input()
input_list = ast.literal_eval(input_str)

# Write your code here
new_lis = [i for i in input_list if i != max(input_list)]
if len(new_lis)==0:
    print("not present")
    
else:
    print(max(new_lis))
