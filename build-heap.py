A = [15, 17, 6, 10, 16, 1, 12, 3, 9, 5]

def Parent(i): 
    return (i - 1) // 2

def Left(i): 
    return 2 * i + 1

def Right(i): 
    return 2 * i + 2

def Heapify(A, i, size):
    L = Left(i)
    R = Right(i)
    if L < size and A[L] < A[i]:
        minps = L
    else:
        minps = i
    if R < size and A[R] < A[minps]:
        minps = R
    if minps != i:
        A[i], A[minps] = A[minps], A[i]
        Heapify(A, minps, size)  # Recur to ensure heap property is maintained

def BuildMinHeap(A):
    size = len(A)
    for i in range((size // 2) - 1, -1, -1):
        Heapify(A, i, size)

print("1) ")
A = [15, 17, 6, 10, 16, 1, 12, 3, 9, 5]
print(A)
BuildMinHeap(A)
print(A)

print("2) ")
B = [16, 14, 13, 17, 2, 8, 5, 9, 15, 3]
print(B)
BuildMinHeap(B)
print(B)