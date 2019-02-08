
# https://codeforces.com/problemset/problem/996/A

bills = [100, 20, 10, 5, 1]

def min_num_bills(n):
    count = 0
    left = n
    for bill in bills:
        count += left // bill
        left = left % bill

    return count

if __name__ == "__main__":
    n = int(input())
    print(min_num_bills(n))

