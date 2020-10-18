# Write a program to reverse an array

'''
Input  : arr[] = [1, 2, 3]
Output : arr[] = [3, 2, 1]

Input :  arr[] = [4, 5, 1, 2]
Output : arr[] = [2, 1, 5, 4]


Approach: (Iterative way)
1) Initialize start and end indexes as start = 0, end = n-1 
2) In a loop, swap arr[start] with arr[end] and change start and end as follows: 
start = start +1, end = end – 1

Time Complexcity is O(log n)
'''

# Implementation

import sys

# by default return a list of string so map, list-int
arr = list(map(int, sys.stdin.readline().strip().split()))


# reading using input() function and list comprehension
#arr = [int(ele) for ele in input().split()]

start = 0
end = len(arr) - 1

while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

print(arr)
