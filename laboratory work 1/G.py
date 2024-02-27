# data = list(map(int, input().split()))

# print(pow(data[0], data[1], ))

module = 987654323

def pow_l(x, n):
    result = 1
    while n != 0:
        if n % 2 != 0:
            result *= x
            result %= module
            n -= 1
        else:
            x *= x
            x %= module
            n /= 2
    return result

a, b = map(int, input().split())

print(pow_l(a, b))

print(pow(100, 100, 987654323))