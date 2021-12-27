"""
    Source for project:     https://projecteuler.net/problem=2
    Name:                   Even Fibonacci Numbers
    Author:                 Logan Brinsmead
    Date:                   December 24, 2021
"""

def evenFibonacci():
    fib=[1,2]
    counter = 0
    while True:
        next = fib[counter] + fib[counter+1]
        fib.append(next) 
        counter += 1
        if fib[-1] > 4000000:
            fib.pop(-1)
            break;
    new = [i for i in fib if i % 2 == 0]
    ans = sum(new)
    print("The answer is: " + str(ans))
    return ans
evenFibonacci()