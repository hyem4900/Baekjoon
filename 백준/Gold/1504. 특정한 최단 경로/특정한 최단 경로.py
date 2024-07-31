# 1504_특정한 최단 경로
# 양방향

from heapq import heappop, heappush

def func(s,e):
    dp = [float("inf")]*(N + 1)
    q = [(0, s)] # 비용, 시작점
    while q:
        c, n = heappop(q)
        if dp[n] < c:
            continue
        for ac, an in adj[n]:
            nc = ac + c
            if nc < dp[an]:
                dp[an] = nc
                heappush(q,(nc, an))
    return dp[e]

N, E = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int,input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))
v1, v2 = map(int,input().split())

if v1 == 1 and v2 == N:
    res1 = func(1, N)
    res2 = res1
else:
    res1 = func(1,v1) + func(v1, v2) + func(v2, N)
    res2 = func(1, v2) + func(v2,v1) + func(v1, N)

ans = min(res1, res2)
if ans == float("inf"):
    print(-1)
    exit()
print(ans)