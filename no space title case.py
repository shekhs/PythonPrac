'''
----------------------------------------------------------------------
Sample input:
caloRie consuMed

Sample output:
Calorie_Consumed

----------------------------------------------------------------------
Sample input:
data science

Sample output:
Data_Science
'''

#take input here
s=input()
s=s.split()
#write code to format the string s as asked 
op=""
for x in s:
    op=op+x.title()+"_"
print(op.strip("_"))

