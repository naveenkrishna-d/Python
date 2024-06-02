# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    for i in range(0,len(A)):
        count=0
        for j in range(0,len(A)):
            if A[i]==A[j]:
                count+=1
        
        if count%2 !=0:
            return A[i]
    return -1

A=[9, 3, 9, 3, 9, 7, 9]
print(solution(A)) 