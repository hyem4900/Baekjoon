import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def func(i, j):
    global ans
    if dp[i][j] != 1:
        return dp[i][j]
    flag = 1
    for di, dj in dir:
        ni = i + di
        nj = j + dj
        if ni in range(N) and nj in range(N) and arr[ni][nj] > arr[i][j]:
            flag = 0
            dp[i][j] = max(dp[i][j], func(ni, nj) + 1)
    if flag:
        return 1
    ans = max(ans, dp[i][j])
    return dp[i][j]

N = int(input()) # 대나무 숲 크기
arr = [list(map(int,input().split())) for _ in range(N)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
dp = [[1]*N for _ in range(N)]
ans = 1
for i in range(N):
    for j in range(N):
        func(i, j)

print(ans)