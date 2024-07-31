from heapq import heappop, heappush
inf = 1e4



tc = 0
while True:
    tc += 1
    N = int(input())
    if not N:
        exit()
    arr = [list(map(int,input().split())) for n in range(N)]
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    dp = [[inf]*N for _ in range(N)]
    dp[0][0] = arr[0][0]
    q = []
    heappush(q,(arr[0][0], 0, 0))
    while q:
        c, i, j = heappop(q)
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if ni in range(N) and nj in range(N):
                nc = c + arr[ni][nj]
                if dp[ni][nj] > nc:
                    dp[ni][nj] = nc
                    heappush(q, (nc, ni ,nj))
    print(f'Problem {tc}: {dp[N-1][N-1]}')