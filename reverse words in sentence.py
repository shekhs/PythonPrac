#Sample input:
#I love coding in python

#Sample output:
#python in coding love I

sentence=input()
s = sentence.split(" ")
op =""
#reverse the words of the sentence here
for x in s[::-1]:
    op=op+x+" "
print(op)
