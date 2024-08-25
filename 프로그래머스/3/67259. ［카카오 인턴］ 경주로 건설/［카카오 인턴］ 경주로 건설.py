from collections import deque
def solution(board):
    N = len(board)
    q = deque() # 좌표, 마지막 이동 방향, 비용
    visited = [[[float("inf")]*N for _ in range(N)] for _ in range(4)]
    for i in range(4):
        visited[i][0][0] = 0
    q.append((0, 0, (1, 0), 0))
    q.append((0, 0, (0, 1), 0))
    while q:
        i, j, last_d, cost = q.popleft()
        k = -1
        for di, dj in (1,0),(0,1),(-1,0),(0,-1):
            k += 1
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and board[ni][nj] == 0:
                last_di = last_d[0]
                # 그 칸으로 가는 새로운 비용 계산
                if last_di ^ di != 0: # 코너 생성되면
                    ncost = cost + 100 + 500
                else:
                    ncost = cost + 100
                if ncost < visited[k][ni][nj]:
                    visited[k][ni][nj] = ncost
                    if ni == N-1 and nj == N-1:
                        break
                    q.append((ni, nj, (di, dj), ncost))

    return min(visited[0][N-1][N-1],visited[1][N-1][N-1],visited[2][N-1][N-1],visited[3][N-1][N-1])
