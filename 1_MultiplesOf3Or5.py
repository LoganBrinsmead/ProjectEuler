"""
    Source for project: https://projecteuler.net/problem=1
    Title:      Multiples Of 3 Or 5
    Module:     Project Euler
    Author:     Logan Brinsmead
    Date:       December 23, 2021
"""

def Multiples():
    
    array = []

    for x in range(1000):
        if x % 3 == 0:
            array.append(x)
        elif x % 5 == 0:
            array.append(x)
    
    print(array)
    print(sum(array))
    return sum(array)

Multiples()