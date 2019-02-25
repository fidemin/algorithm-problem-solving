
from collections import Counter

def is_possible(n, counter):
    dup_4_arr = []
    dup_2_arr = []
    only_one_value = None
    if n & 1 == 0:
        for v in counter.values():
            if v % 4 != 0:
                return (False, dup_4_arr, dup_2_arr, only_one_value)
    else:
        #for 4
        count_4 = 0
        min_count_4 = (n // 2)**2
        for k, v in counter.items():
            while (v >= 4):
                v = v - 4
                count_4 += 1
                counter[k] -= 4
                dup_4_arr.append(k)
                if count_4 == min_count_4:
                    break

            if count_4 == min_count_4:
                break

        if count_4 < min_count_4:
            return (False, dup_4_arr, dup_2_arr, only_one_value)

        # for 2
        count_2 = 0
        min_count_2 = (n // 2) * 2
        for k, v in counter.items():
            while (v >= 2):
                v = v - 2
                count_2 += 1
                counter[k] -= 2
                dup_2_arr.append(k)
                if count_2 == min_count_2:
                    break

            if count_2 == min_count_2:
                break

        if count_2 < min_count_2:
            return (False, dup_4_arr, dup_2_arr, only_one_value)

        for k, v in counter.items():
            if v == 1:
                only_one_value = k

    return True, dup_4_arr, dup_2_arr, only_one_value


def make_matrix(n, arr, counter, dup_4_arr, dup_2_arr, only_one_value):
    ret = [["-1"] * n for _ in range(n)]
    arr = sorted(arr)
    if n & 1 == 0:
        current = 0
        for i in range(n//2):
            for j in range(n//2):
                ret[i][j] = str(arr[current])
                current += 1
                ret[i][n-1-j] = str(arr[current])
                current += 1
                ret[n-1-i][j] = str(arr[current])
                current += 1
                ret[n-1-i][n-1-j] = str(arr[current])
                current += 1

    else:
        # for 4
        current_4 = 0
        for i in range(n//2):
            for j in range(n//2):
                ret[i][j] = str(dup_4_arr[current_4])
                ret[i][n-1-j] = str(dup_4_arr[current_4])
                ret[n-1-i][j] = str(dup_4_arr[current_4])
                ret[n-1-i][n-1-j] = str(dup_4_arr[current_4])
                current_4 += 1

        current_2 = 0
        center = n//2
        for i in range(n//2):
            ret[center][i] = str(dup_2_arr[current_2])
            ret[center][n-1-i] = str(dup_2_arr[current_2])
            current_2 += 1

        for i in range(n//2):
            ret[i][center] = str(dup_2_arr[current_2])
            ret[n-1-i][center] = str(dup_2_arr[current_2])
            current_2 += 1

        ret[center][center] = str(only_one_value)


    return ret

if __name__ == "__main__":
    n = int(input())
    arr = tuple(map(int, input().split(" ")))
    counter = Counter(arr)
    possible, dup_4_arr, dup_2_arr, only_one_value = is_possible(n, counter)
    if possible:
        print("YES")
        mat = make_matrix(n, arr, counter, dup_4_arr, dup_2_arr, only_one_value)
        for i in range(n):
            print(" ".join(mat[i]))
    else:
        print("NO")
