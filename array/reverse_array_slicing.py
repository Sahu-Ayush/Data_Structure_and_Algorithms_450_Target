# Write a program to reverse an array

'''
Input  : arr[] = [1, 2, 3]
Output : arr[] = [3, 2, 1]

Input :  arr[] = [4, 5, 1, 2]
Output : arr[] = [2, 1, 5, 4]


Approach: Slicing
arr[::-1]

Time Complexcity is O(n)
'''

# Implementation
import sys

# by default return a list of string so map, list-int
arr = list(map(int, sys.stdin.readline().strip().split()))

# reading usind input() function and list comprehension
#arr = [int(ele) for ele in input().split()]

print(arr[::-1])
