#!/usr/bin/python 3
""" method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    """
    n = len(boxes)  # Total number of boxes
    visited = [False] * n  # Create a list to keep track of visited boxes
    visited[0] = True  # Mark the first box as visited
    queue = [0]  # Create list as a queue and initialize it with the first box

    while queue:
        current_box = queue.pop(0)  # Get current box frm d front of the queue

        # Check all the keys in the current box
        for key in boxes[current_box]:
            if key >= 0 and key < n and not visited[key]:
                # If key is valid&leads to an unvisited box,mark it as visited
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited
    return all(visited)
