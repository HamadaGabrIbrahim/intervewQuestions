"""
Given a number represented as a list, increment the number by one.

input [2, 7, 9]
output [2, 8, 0]

input [3, 6, 8]
output [3, 6, 9]

input [9, 9, 9, 9]
output [1, 0, 0, 0, 0]

Time complexity is O(n)
"""


def increment_by_one(num_as_list):
    num_as_list[-1] += 1
    for index in reversed(range(1, len(num_as_list))):
        if num_as_list[index] != 10:
            break
        num_as_list[index] = 0
        num_as_list[index - 1] += 1
    if num_as_list[0] == 10:
        num_as_list[0] = 0
        num_as_list.insert(0, 1)
    return num_as_list
