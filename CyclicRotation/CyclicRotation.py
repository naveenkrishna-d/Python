#take arr and len of array, iterate from 0 index to length 
def solution(A,K):
    # for range of k set the first element of the array to the last and shift the rest elements to the right
    for _ in range(K):
        A = [A[-1]]+A[:-1]
    
    return A

A =[3, 8, 9, 7, 6]
K=3
print(solution(A,K))

