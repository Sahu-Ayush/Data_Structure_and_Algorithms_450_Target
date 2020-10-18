# Write a program to reverse an string

'''
Input  : pythonstring
Output : gnirtsnohtyp

Input  : hannah
Output : hannah

Approach: Slicing
arr[::-1]

Time Complexcity is O(n)
'''

# Implementation
import sys

# by default return a list of string so map
#s = sys.stdin.readline().strip()

# reading using input() function
s = input().strip()

print(s[::-1])
