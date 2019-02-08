
# https://codeforces.com/problemset/problem/1111/A

vowels = set(["a", "e", "i", "o", "u"])

def can_partial_transform(c1, c2):
    if (c1 in vowels and c2 in vowels) or (c1 not in vowels and c2 not in vowels):
        return True
    return False

def can_transform(hero1, hero2):
    hero1_len = len(hero1)
    if hero1_len != len(hero2):
        return False

    for i in range(hero1_len):
        if not can_partial_transform(hero1[i], hero2[i]):
            return False

    return True

if __name__ == "__main__":
    hero1 = input()
    hero2 = input()
    result = can_transform(hero1, hero2)
    if result:
        print('Yes')
    else:
        print('No')
