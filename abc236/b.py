N = int(input())
A = [int(x) for x in input().split()]

xs = [0] * (N + 1)
 
for a in A:
    xs[a] += 1

result = 0

for i, x in enumerate(xs):
    if x == 3:
        result = i
        break

print(result)
