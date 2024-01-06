'''
Sum of Primes
###
Description
Write python code to find the sum of prime numbers from 2 to n where n is a positive integer entered by the user.

Note: n can be non-prime or prime. You have to find sum of primes till n and not sum of n prime numbers. i.e. for input 10, output should be 17.

Hint: You can try using lambda functions and comprehensions to reduce the lines of code you have to write.



Input: A positive integer n.

Output: A integer denoting the sum of primes less than or equal to n



Sample Input:

5

Sample Output:

10
'''


n=int(input())#find the sum of primes from 2 to n 
def checkPrime(n):
    for x in range(2,n):
        if n%x==0:
            return False
    return True

primes = []
for x in range(2,n+1):
    if checkPrime(x):
        primes.append(x)

print(sum(primes))
