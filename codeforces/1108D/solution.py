
def is_diverse(left, mid):
    return left != mid

def diverse_lamp_color(left, right=None):
    init_set = set(["R", "G", "B"])
    return init_set.difference(set([left, right])).pop()

def diverse_gardland(lamps):
    lamps = list(lamps)
    count = 0
    for i in range(1, len(lamps)):
        if not is_diverse(lamps[i-1], lamps[i]):
            if i == len(lamps)-1:
                lamps[i] = diverse_lamp_color(lamps[i-1])
            else:
                lamps[i] = diverse_lamp_color(lamps[i-1], lamps[i+1])
            count += 1
    return ("".join(lamps), count)


if __name__ == "__main__":
    n = int(input())
    lamps = input()
    lamps, count = diverse_gardland(lamps)
    print(count)
    print(lamps)
