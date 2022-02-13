N, M = [int(x) for x in input().split()]
S = [x for x in input().split()]
T = [x for x in input().split()]

xs = set(T)

for s in S:
    if s in xs:
        print("Yes")
    else:
        print("No")

