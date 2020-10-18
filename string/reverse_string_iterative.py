# Write a program to reverse an string

'''
Input  : pythonstring
Output : gnirtsnohtyp

Input  : hannah
Output : hannah

Approach: (Iterative way)
1) Initialize start and end indexes as start = 0, end = n-1 
2) In a loop, swap arr[start] with arr[end] and change start and end as follows: 
start = start +1, end = end – 1

Time Complexcity is O(n)
'''

# Implementation

# reading using input() function and convert into list of char
s = list(input().strip())

start = 0
end = len(s) - 1

while start < end:
    s[start], s[end] = s[end], s[start]
    start += 1
    end -= 1

rs = "".join(s)

print(rs)
