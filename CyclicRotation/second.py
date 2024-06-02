def solution(A,K):
    #store last element in a variable
    def rotate(A):
        n=len(A)
        last=A[n-1]
        #iterate over from last index to first decreasing each index and shift each element to the right.
        for i in range(n-1,0,-1):
            A[i]=A[i-1]

        #place the last elementin the first
        A[0]=last

    for j in range(K):
        rotate(A)

    return A

A = [3, 8, 9, 7, 6]
K=3
print(solution(A,K))