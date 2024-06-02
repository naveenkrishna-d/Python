import numpy as np

arr = np.array([1,2,3,4,5])

print(f"original: {arr}")
print(f"add 5: {arr+5}")
print(f"Multiple by 5: {arr*5}")

print(f"Mean: {np.mean(arr)}")
print(f"sd: {np.std(arr)}")

matrix = np.array([[1,2,3],[4,5,6]])
print(f"2D matrix:\n{matrix}")

print(f"transpose:\n{np.transpose(matrix)}")

