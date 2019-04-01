

def kth_common_divisor(a, b, k):
    min_ = min(a, b)
    divisors = []

    for i in range(1, min_+1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)

    return divisors[-k]


if __name__ == "__main__":
    a, b, k = map(int, input().split())
    print(kth_common_divisor(a, b, k))
