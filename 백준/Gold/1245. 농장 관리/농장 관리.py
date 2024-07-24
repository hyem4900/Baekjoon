from collections import deque
# 산봉우리인지 판별하는 함수
def bfs(si, sj):
    global ans
    dir = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
    q = deque()
    q.append((si,sj))
    while q:
        i, j = q.popleft()
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            # 상하좌우대각선 탐색 -> 높이 같으면 큐에 추가. 다르고 ni,nj 높이가 더 높으면 봉우리 아님
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
                visited[ni][nj] = 1
                if arr[ni][nj] > arr[i][j]:
                    return
                elif arr[ni][nj] == arr[i][j]:
                    nocheck[ni][nj] = 1
                    q.append((ni,nj))
    ans += 1
    return

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
nocheck = [[0]*M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        visited = [[0] * M for _ in range(N)]
        if not nocheck[i][j]:
            visited[i][j] = 1
            bfs(i,j)
print(ans)