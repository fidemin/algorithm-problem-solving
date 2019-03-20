
# refers to editorial
def xor_world(A, B):
    if A == 0:
        m  = (B+1) // 2
        pre = 0 if m % 2 == 0 else 1
        if B % 2 == 1:
            return pre
        else:
            return pre ^ B

    else:
        return xor_world(0, A-1) ^ xor_world(0, B)


if __name__ == "__main__":
    A, B = map(int, input().split())
    print(xor_world(A, B))

