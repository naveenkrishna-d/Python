def solution(A):
    # Initialize result
    rec=0
    # Traverse the array
    for i in A:
        # XOR with the result
        rec=rec^i
    return rec

A=[9,3,9,3,9,7,9]
print(solution(A))