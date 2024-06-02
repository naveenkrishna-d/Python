def solution(A):
    #find length of array
    n=len(A)
    #create dict to store the elements of array as key and count of elements as values
    hash=dict()

    #iterate over the index of elements of array A[] and find the count of each element
    for i in range(0,n):
        hash[A[i]] =hash.get(A[i],0)+1

    #ierate over the key of hash and divide the value of hash to find the odd occurence and return it   
    for i in hash:
        if hash[i]%2!=0:
            return i
    
    #return any other error
    return -1

A =[2, 3, 5, 4, 5, 2, 4,3, 5, 2, 4, 4, 2]
print(solution(A))