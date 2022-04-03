def countOperations(A):
    count = 0
    for i in range(len(A)-2):
        if A[i] != A[i+2]:
            count += 1
    return count

ls = [int(x) for x in input().split()]
print(countOperations(ls))