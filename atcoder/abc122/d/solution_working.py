
count = 0
agc_family = set(["AGC", "ACG", "GAC"])
agct = ["A", "G", "C", "T"]

def we_like_agc(n, prev):
    if n == 0:
        print(prev)
        return

    global count

    for c in agct:
        new_prev = prev + c
        if new_prev[-3:] in agc_family:
            count += 1

        we_like_agc(n-1, new_prev)


if __name__ == "__main__":
    we_like_agc(4, '')
    print(count)

