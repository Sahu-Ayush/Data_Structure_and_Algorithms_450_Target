# Write a program to reverse an array

'''
Input  : pythonstring
Output : gnirtsnohtyp

Input  : hannah
Output : hannah

Approach: (Recursive way)
1) Initialize start and end indexes as start = 0, end = n-1 
2) Swap arr[start] with arr[end] 
3) Recursively call reverse for rest of the array.

Time Complexcity is O(n)
'''

# Implementation
import sys

def reverseArray(str_lst, start, end):
    
    if start >= end:
        return

    str_lst[start], str_lst[end] = str_lst[end], str_lst[start]

    reverseArray(str_lst, start+1, end-1)


# Main

# by default return a list of string
s = sys.stdin.readline().strip()
str_lst = list(s)

# reading using input() function and list comprehension
#s = input().strip()
#str_lst = list(s)

# calling function
reverseArray(str_lst, 0, len(str_lst)-1)
rs = "".join(str_lst)
print(rs)
