N = int(input())
A = [[int(x) for x in input().split()] for _ in range(2*N - 1)]

def solve(N, A):

    ss = [[0] * (i+1) + row for i, row in enumerate(A)] + [[0]*(2*N)]

    def calc(xs):
        a = xs[0]
        for i in range(1, len(xs)):
            b = xs[i]
            rxs = xs[1:i] + xs[i + 1:]
            r = ss[a][b]
            if rxs:
                for q in calc(rxs):
                    yield r ^ q
            else:
                yield r

    xs = tuple(range(2*N))
    result = max(x for x in calc(xs))

    print(result)

solve(N, A)