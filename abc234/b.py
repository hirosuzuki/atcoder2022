import math

N = int(input())
XY = [[int(x) for x in input().split()] for i in range(N)]

result = 0

for i in range(N):
    for j in range(i + 1, N):
        r = math.sqrt((XY[i][0] - XY[j][0])**2 +  (XY[i][1] - XY[j][1])**2)
        result = max(result, r)

print(result)
