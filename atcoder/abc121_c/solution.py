
import heapq

def energy_drink_collector(M, heap):
    left = M
    ret = 0

    while left:
        ele = heapq.heappop(heap)
        deduct = min(left, ele[1])
        ret += ele[0] * deduct
        left -= deduct

    return ret


if __name__ == "__main__":
    N, M = map(int, input().split())

    heap = []
    for _ in range(N):
        a, b = map(int, input().split())
        heapq.heappush(heap, (a, b))

    result = energy_drink_collector(M, heap)
    print(result)
