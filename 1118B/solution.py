
'''
def candies(n, arr):
    count = 0
    for i in range(n):
        even = True
        sum_even = 0
        sum_odd = 0
        for j in range(n):
            if i == j:
                continue

            if even:
                sum_even += arr[j]
                even = False
            else:
                sum_odd += arr[j]
                even = True
        if sum_odd == sum_even:
            count += 1
    return count
'''

def make_to_left(n, arr):
    flag = True
    ret = [-1]*n

    flag_sum = 0
    not_flag_sum = 0
    for i in range(n-1, -1, -1):
        if flag:
            flag_sum += arr[i]
            ret[i] = flag_sum
            flag = False
        else:
            not_flag_sum += arr[i]
            ret[i] = not_flag_sum
            flag=True

    return ret


def make_to_right(n, arr):
    flag = True
    ret = [-1]*n

    flag_sum = 0
    not_flag_sum = 0
    for i in range(n):
        if flag:
            flag_sum += arr[i]
            ret[i] = flag_sum
            flag = False
        else:
            not_flag_sum += arr[i]
            ret[i] = not_flag_sum
            flag=True

    return ret

def candies(n, arr):
    to_left = make_to_left(n, arr)
    to_right = make_to_right(n, arr)

    ret = 0
    for i in range(n):
        even = 0
        odd = 0
        if i < n-1:
            even += to_left[i+1]
        if i < n-2:
            odd += to_left[i+2]
        if i > 1:
            even += to_right[i-2]
        if i > 0:
            odd += to_right[i-1]
        if even == odd:
            ret += 1

    return ret


if __name__ == "__main__":
    n = int(input())
    arr = [int(a) for a in input().split(" ")]
    ret = candies(n, arr)
    print(ret)
