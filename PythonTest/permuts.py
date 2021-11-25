#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

def permuts(data: [int]) -> [[int]]:
    if len(data) == 0:
        return [[]]

    result = []
    for i, num in enumerate(data):
        rest = data[:i] + data[i + 1:]
        for partial in permuts(rest):
            result.append([num] + partial)
    return result

print(permuts([1,2,3,4,5,6,7,8,9]))
