#take the input here
number=int(input())
#
#the function definition starts here
def factorial(n):
    #write the funtion here that finds and RETURNS factorial of next
    if n<0:
        return -1
    if n==0:
        return 1
    return n*factorial(n-1)    
    


#function definition ends here

#do not alter the code typed below
k=factorial(number)
print(k)
