S = input()
a, b = [int(x) for x in input().split()]

xs = list(S)
xs[a - 1], xs[b - 1] = xs[b - 1], xs[a - 1]
result = "".join(xs)

print(result)
