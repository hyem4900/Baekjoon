from heapq import heappop, heappush
inf = 1e4


def sol(arr, cnt, n, x=0, y=0):
    for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        nx, ny = x + dx, y + dy
        if nx in range(n) and ny in range(n):
            tmp = dp[x][y] + arr[nx][ny]
            if tmp >= dp[nx][ny]:continue
            dp[nx][ny] = tmp
            heappush(q, (tmp, nx, ny))

i = 1
while True:
    n = int(input())
    if not n:exit()
    dp, arr = [[inf] * n for _ in range(n)], [list(map(int, input().split())) for _ in range(n)]
    dp[0][0] = arr[0][0]
    q = []
    heappush(q, (dp[0][0], 0, 0))   # 요금, 좌표
    while q:
        cost, x, y = heappop(q)
        sol(arr, cost, n, x, y)
    print(f'Problem {i}: {dp[-1][-1]}')
    i += 1