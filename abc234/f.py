from re import I


S = input()

M = 998244353
L = 5030

Fm = {}
inverseFm = {}
x = 1
for i in range(L):
    Fm[i] = x
    x = x * (i + 1) % M

def inverseFm(x, cache={}):
    if x in cache:
        return cache[x]
    result = pow(Fm[x], M - 2, M)
    cache[x] = result
    return result

def C(n, r):
    result = Fm[n] * inverseFm(r) * inverseFm(n - r) % M
    return result

ns = [0] * 26

for c in S:
    ns[ord(c) - 97] += 1


lrs = 5030
rs = [0] * lrs
rs[0] = 1
for n in ns:
    if n == 0:
        continue
    nrs = [0] * lrs
    for i, m in enumerate(rs):
        if m == 0:
            break
        for j in range(n + 1):
            nrs[i + j] = (nrs[i + j] + m * C(i + j, j)) % M
    rs = nrs
    # print(n, rs)

result = (sum(rs) - 1) % M
print(result)
