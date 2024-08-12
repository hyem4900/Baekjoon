import sys
sys.setrecursionlimit(10_000)

input = sys.stdin.readline
#printf = sys.stdout.write

drdc = ((-1, 0), (0, 1), (1, 0), (0, -1))

def dfs(r, c):
    global N, board, visited
    ans = 0
    v = board[r][c]
    ans = 1
    for dr, dc in drdc:
        if 0<=(nr:=r+dr)<N and 0<=(nc:=c+dc)<N and board[nr][nc]>v:
            if visited[nr][nc]:
                ans =  max(ans, 1+visited[nr][nc])
            else:
                ans = max(ans, 1+dfs(nr, nc))
    visited[r][c] = ans
    return ans

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*(N) for _ in range(N)]

for rs in range(N):
    for cs in range(N):
        if visited[rs][cs]:
            continue
        dfs(rs, cs)
print(max(map(max, visited)))