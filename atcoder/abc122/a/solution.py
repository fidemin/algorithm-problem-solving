

def double_helix(b):
    if b == 'A':
        return 'T'

    if b == 'T':
        return 'A'

    if b == 'C':
        return 'G'

    if b == 'G':
        return 'C'


if __name__ == "__main__":
    b = input()
    print(double_helix(b))
