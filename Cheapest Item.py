'''
Problem Statement
#
Description
You will be given a dictionary with keys as items and values as their prices. You have to print the cheapest item. 
####
--------------------------------------------------------------------------
######

Sample input:
A single line non-empty dictionary
Sample output:
cheapest_item name: cheapest_item_cost
###
--------------------------------------------------------------------------
Sample input:
{'mobile1':10000, 'mobile2':11000, 'mobile3':13000, 'mobile4':9000, 'mobile5':15000, 'mobile6':16000, 'mobile7':17000, 'mobile8':18000, 'mobile9':19000}

Sample output:
mobile4: 9000

Note: in case of a tie, whichever item came first should be the output.
'''
###
import ast
#take input here
d = ast.literal_eval(input())
#
pr =[]
both =[]
for x in d:
    pr.append(d[x])
    both.append(x+": "+str(d[x]))
m = both[pr.index(min(pr))]    

#start writing your code here
print(m)
