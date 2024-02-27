n = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += A[i] * (i+1) * (n-i)

print(ans)