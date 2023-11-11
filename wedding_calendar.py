#taking input
import ast
input_str1 = input()
input_list1 = ast.literal_eval(input_str1)
events = input_list1
##
wedding = int(input())

#start writing from here
clash = 0
for x in events:
    if wedding in range(x[0],x[1]+1):
        clash += 1
print(clash)




