def count_ropes(ropes, length):
    count = 0
    for rope in ropes:
        count += rope // length
    return count

def max_rope_length(ropes, k):
    left = 1
    right = max(ropes)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if count_ropes(ropes, mid) >= k:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result

n, k = map(int, input().split())
ropes = [int(input()) for _ in range(n)]
result = max_rope_length(ropes, k)

print(result)