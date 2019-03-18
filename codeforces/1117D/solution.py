# failed with time limit

m = 0
cache = [-1] * 101

def magic_gems(n):
    for i in range(1, m):
        cache[i] = 1

    cache[0] = 2

    for i in range(m+1, n+1):
        ret = cache[(i-1)%m] + cache[(i-m)%m]
        ret = ret % 1000000007
        cache[i%m] = ret

    return cache[n%m]


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    result = magic_gems(n)
    print(result)
