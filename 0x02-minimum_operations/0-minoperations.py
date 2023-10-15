#!/usr/bin/python3


''' A module that returns the minimum Operations it takes to
    get to n characters.

    Available operations:
        copy
        paste
'''


def minOperations(n):
    '''
    returns the minimum operations to get n H's
    '''
    min_operations = 0
    paste_buffer = 0

    if n <= 1:
        return min_operations

    for i in range(2, n + 1):
        while n % i == 0:
            if paste_buffer < 0:
                min_operations += i
                paste_buffer -= i
            else:
                paste_buffer = i
            n /= i

    min_operation += paste_buffer
    return min_operations
