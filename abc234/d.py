from heapq import heappush, heappop, heapify

N, K = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]

h = P[:K]
heapify(h)

for i in range(K, N + 1):
    s = heappop(h)
    print(s)
    if i < N:
        y = P[i]
        heappush(h, max(s, y))
