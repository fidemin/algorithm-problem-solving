
def two_max(max_arr, value):
    if max_arr[0] < value:
        max_arr[1] = max_arr[0]
        max_arr[0] = value
    elif max_arr[1] < value:
        max_arr[1] = value
    return max_arr


def emotes(n, m, k, arr):
    max_arr = [0, 0]
    for ele in arr:
        max_arr = two_max(max_arr, ele)

    return (m // (k + 1)) * (max_arr[0] * k + max_arr[1]) + (m % (k+1)) * max_arr[0]


if __name__ == "__main__":
    n, m, k = map(int, input().split(" "))
    arr = map(int, input().split(" "))
    result = emotes(n, m, k, arr)
    print(result)
