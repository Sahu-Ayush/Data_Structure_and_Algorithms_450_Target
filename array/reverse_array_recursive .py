# Write a program to reverse an array

'''
Input  : arr[] = [1, 2, 3]
Output : arr[] = [3, 2, 1]

Input :  arr[] = [4, 5, 1, 2]
Output : arr[] = [2, 1, 5, 4]


Approach: (Recursive way)
1) Initialize start and end indexes as start = 0, end = n-1 
2) Swap arr[start] with arr[end] 
3) Recursively call reverse for rest of the array.

Time Complexcity is O(n)
'''

# Implementation
import sys

def reverseArray(arr, start, end):
    
    if start >= end:
        return

    arr[start], arr[end] = arr[end], arr[start]

    reverseArray(arr, start+1, end-1)

# Main

# by default return a list of string so map, list-int
arr = list(map(int, sys.stdin.readline().strip().split()))

# reading using input() function and list comprehension
#arr = [int(ele) for ele in input().split()]

# calling function
reverseArray(arr, 0, len(arr)-1)
print(arr)
