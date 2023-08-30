'''

'''
input data
'''


Sample input:
{‘Mobile’: [‘Redmi’, ‘Samsung’, ‘Realme’], 
‘Laptop’: [‘Dell’, ‘HP’],
‘TV’: [‘Videocon’, ‘Sony’] }

Sample output:
[‘Mobile_Redmi’, ‘Mobile_Samsung’, ‘Mobile_Realme’, ‘Laptop_Dell’, ‘Laptop_HP’, ‘TV_Videocon’, ‘TV_Sony’]

Sample input:
{ 'Pen': ['Gel', 'Ink', 'ball'],
'Mobile': ['Android', 'apple'] }

Sample output:
['Pen_Gel', 'Pen_Ink', 'Pen_ball', 'Mobile_Android', 'Mobile_apple']
'''

#input has been taken for you
import ast
input_str = input()
#input dictionary has been received in input_dict
input_dict = ast.literal_eval(input_str)
ans=[]
for x in input_dict:
    for y in input_dict[x]:
        ans.append(x+"_"+y)
print(ans)

#start writing your code here


