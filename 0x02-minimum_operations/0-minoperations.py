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

    for i in range(2, n + 1):
        while n % i == 0:
            if paste_buffer > 0:
                # If there's content in the paste buffer, we can paste it
                min_operations += 1
                paste_buffer -= 1
            else:
                # Otherwise, we need to copy everything
                paste_buffer = i
            n /= i

    min_operations += paste_buffer  # Paste the remaining content in the buffer
    return min_operations
