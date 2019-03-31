
cache = None

def make_cache(string):
    global cache

    n = len(string)
    cache = [-2] * n

    prev = None
    count = 0

    for i, c in enumerate(string):
        if c == 'C' and prev == 'A':
            count += 1

        cache[i] = count
        prev = c


if __name__ == "__main__":
    N, Q = map(int, input().split())
    string = input()
    make_cache(string)

    for _ in range(Q):
        l, r = map(int, input().split())
        print(cache[r-1] - cache[l-1])
