#!/usr/bin/python3
"""This is a function for Pascal triangle"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s triangle of n
    
    Parameters:
        n (int): The number of rows to generate in Pascal's Triangle.
    """

    if n <= 0:
        return []

pascal_triangle = [1]
while len(pascal_triangle) != n:
    previous = pascal_triangle[-1]
    current = [1]
    for i in range(len(previous) - 1):
        current.append(previous[i] + previous[i + 1])
    current.append(1)
    pascal_triangle.append(current)
return pascal_triangle