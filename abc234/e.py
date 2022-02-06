X = int(input())

def solve(X: int):
    s = str(X)
    l = len(s)
    if l == 1:
        print(X)
        return
    for c1 in range(int(s[0]), 10):
        for j in range(-9, 10):
            cl = c1 + j * (l - 1)
            if not (0 <= cl < 10):
                continue
            ss = int("".join([str(c1 + j * k) for k in range(l)]))
            if ss >= X:
                print(ss)
                return

solve(X)
