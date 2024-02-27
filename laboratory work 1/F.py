N, K = map(int, input().split())  
array1_sorted = list(map(int, input().split()))  
array2 = list(map(int, input().split())) 

def binary_search(A, number, N):
    left = 0
    right = N

    while left <= right:
        middle = (left + right) // 2

        if A[middle] == number:
            return True
        elif A[middle] < number:
            left = middle + 1
        else:
            right = middle - 1

    return False

if __name__ == '__main__':
    for element in array2: #каждое из второго ищется в первом
        if binary_search(array1_sorted, element, N):
            print("YES")
        else:
            print("NO")