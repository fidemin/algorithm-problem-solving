

def atcoder(string):
    acgt = set('ACGT')
    on_count = False
    count = 0
    max_count = 0

    for c in string:
        if c in acgt:
            if not on_count:
                on_count = True
            count += 1
        else:
            if on_count:
                on_count = False
                max_count = max(max_count, count)
                count = 0

    if on_count:
        max_count = max(max_count, count)

    return max_count


if __name__ == "__main__":
    string = input()
    print(atcoder(string))
