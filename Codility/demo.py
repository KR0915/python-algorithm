# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A.sort()
    j=1
    for n in A:
        if n==j:
            j+=1
        
    return j
    pass
