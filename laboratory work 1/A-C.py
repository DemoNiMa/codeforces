def max_sum(n, A):
    max_sum = A[0]
    curr_sum = A[0]
    max_start_index = max_end_index = curr_start_index = 0

    for i in range(1, n):
        if curr_sum < 0:
            curr_sum = A[i]
            curr_start_index = i
        else:
            curr_sum += A[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            max_start_index = curr_start_index
            max_end_index = i

    print(max_sum)
    print(max_start_index + 1, max_end_index + 1)

n = int(input())
A = list(map(int, input().split()))
max_sum(n, A)