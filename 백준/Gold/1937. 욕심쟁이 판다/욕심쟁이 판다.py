import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
def func(i, j):
    mx = 1
    for di, dj in dir:
        ni, nj = i + di, j + dj
        if ni in range(N) and nj in range(N) and arr[ni][nj] > arr[i][j]:
            if not dp[ni][nj]:
                mx = max(mx, func(ni, nj) + 1)
            else:
                mx = max(mx, dp[ni][nj] + 1)
    dp[i][j] = mx
    return mx

N = int(input()) # 대나무 숲 크기
arr = [list(map(int,input().split())) for _ in range(N)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
dp = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not dp[i][j]:
            func(i, j)

print(max(map(max, dp)))