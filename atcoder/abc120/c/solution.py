
from collections import deque

def unification(string):

    n = len(string)

    if n == 1:
        return 0

    q = deque()
    idx = 2
    q.appendleft(string[0])
    q.appendleft(string[1])
    count = 0

    while idx < n:
        while len(q) > 1 and q[0] != q[1]:
            q.popleft()
            q.popleft()
            count += 2

        q.appendleft(string[idx])
        idx += 1

    if len(q) > 1 and q[0] != q[1]:
        q.popleft()
        q.popleft()
        count += 2

    return count


if __name__ == "__main__":
    string = input()
    print(unification(string))

