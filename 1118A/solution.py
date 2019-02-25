
def water_buying(n, a, b):
    a_per_l = a
    b_per_l = b / 2

    if a_per_l <= b_per_l:
        return a * n
    else:
        num_b = n // 2
        ret = (n // 2) * b + (n % 2) * a
        return int(ret)


if __name__ == "__main__":
    q = int(input())

    for i in range(q):
        n, a, b = map(int, input().split(" "))
        ret = water_buying(n, a, b)
        print(ret)
