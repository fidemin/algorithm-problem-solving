

def white_cells(H, M, h, m):
    return H*M - h*M - m*H + h*m


if __name__ == "__main__":
    HM = list(map(int, input().split()))
    H = HM[0]
    M = HM[1]
    hm = list(map(int, input().split()))
    h = hm[0]
    m = hm[1]

    ret = white_cells(H, M, h, m)
    print(ret)
