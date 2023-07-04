'''
##
Problem : 
Flatten a dictionary
Description
Consider a nested dictionary as follows:
##
{'Fruit': 1, 'Vegetable': {'Cabbage': 2, 'Cauliflower': 3}, 'Spices': 4}
#
Your task is to flatten a nested dictionary and join the nested keys with the "_" character. For the above dictionary, the flattened dictionary would be as follows:
###
{'Fruit': 1, 'Vegetable_Cabbage': 2, 'Vegetable_Cauliflower': 3, 'Spices': 4}
###
The input will have a nested dictionary.
The output should have two lists. The first list will have keys and the second list should have values. Both lists should be sorted.
Sample Input:

{'Fruit': 1, 'Vegetable': {'Cabbage': 2, 'Cauliflower': 3}, 'Spices': 4}
Sample Output:
['Fruit', 'Spices', 'Vegetable_Cabbage', 'Vegetable_Cauliflower']
[1, 2, 3, 4]
You will find the inbuilt function isinstance() of python quite useful here. Read more about it here.
###

'''
import ast,sys
input_str = sys.stdin.read()
input_dict = dict(ast.literal_eval(input_str))
ans={}
#{'Fruit': 1, 'Vegetable': {'Cabbage': 2, 'Cauliflower': 3}, 'Spices': 4}
def flatten_dict(dd, separator='_', prefix=''):
    #complete this function
    for x in dd:
        if isinstance(dd[x], int):
            ans[x]=dd[x]
        else:
            for xx in dd[x]:
                ans[x+separator+xx]=dd[x][xx]
    return ans           

out1=list(flatten_dict(input_dict).keys())
out2=list(flatten_dict(input_dict).values())
out1.sort()
out2.sort()
print(out1)
print(out2)

