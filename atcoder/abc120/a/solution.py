
def favorite_sound(A, B, C):
    return min(B//A, C)

if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(favorite_sound(A, B, C))
