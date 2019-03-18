

def best_segment(n, arr):
    max_value = 0
    current_count = 0
    max_count = 0
    for i, ele in enumerate(arr):
        if ele > max_value:
            max_value = ele
            current_count = 1
            max_count = 1
        elif ele == max_value:
            current_count += 1
            if i == n - 1:
                max_count = max([max_count, current_count])
        else:
            max_count = max([max_count, current_count])
            current_count = 0

    return max_count


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split(" "))
    result = best_segment(n, arr)
    print(result)
