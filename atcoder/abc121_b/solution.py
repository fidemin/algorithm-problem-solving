
def multiply(A, B):
    ret = 0
    for i in range(len(A)):
        ret += A[i]*B[i]

    return ret


def can_you_solve_this(A, B, C):
    return multiply(A, B) + C > 0


if __name__ == "__main__":
    N, M, C = map(int, input().split())

    B = list(map(int, input().split()))

    count = 0
    for i in range(N):
        A = list(map(int, input().split()))
        if can_you_solve_this(A, B, C):
            count += 1

    print(count)
