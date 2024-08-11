# 방향을 소수곱으로 저장하기
# 상 하 좌 우에 각각 2, 3, 5, 7 할당

from collections import deque

def sol():
    for aci, acj in ACs:
        q = deque()
        for d in [2,3,5,7]:
            q.append((aci, acj, d))
        while q:
            i, j, d = q.popleft()
            ni = i + dir[d][0]
            nj = j + dir[d][1]
            if ni in range(N) and nj in range(M):
                if visited[ni][nj] % d != 0: # 해당 칸을 현재 방향으로 방문한 적 없다면
                    visited[ni][nj] = visited[ni][nj] * d
                    if arr[ni][nj] == 1 and (d == 7 or d == 3):
                        continue
                    if arr[ni][nj] == 2 and (d == 5 or d == 2):
                        continue
                    q.append((ni, nj, obj_dir[arr[ni][nj]][d]))

def countAns():
    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 1:
                ans += 1
    return ans

N, M = map(int,input().split()) # 맵 크기 NxM
arr = [list(map(int,input().split())) for _ in range(N)]
dir = {2:(-1,0),3:(0,1),5:(1,0),7: (0,-1)} # 상2, 우3, 하5, 좌7
obj_dir = [
    {2: 2, 3: 3, 5: 5, 7: 7},
    {2: 2, 3: 7, 5: 5, 7: 3}, # 1 좌우 바뀜
    {2: 5, 3: 3, 5: 2, 7: 7}, # 2 상하 바뀜
    {2: 3, 3: 2, 5: 7, 7: 5}, # 3 상우, 하좌끼리 바뀜
    {2: 7, 3: 5, 5: 3, 7: 2}, # 4 상좌, 하우끼리 바뀜
]

ACs = []
visited = [[1]*M for _ in range(N)]
# 에어컨 위치 찾기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 9:
            visited[i][j] = 210
            ACs.append((i, j))

sol()

ans = countAns()

print(ans)