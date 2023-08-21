#you have to take input on your own here
import ast
team = ast.literal_eval(input())
appli = ast.literal_eval(input())
##

#write your code here
def team_improve(team,a):
    av = sum(team)/len(team)
    if a>av:
        team.append(a)

for x in appli:
    team_improve(team,x)


print(team)
