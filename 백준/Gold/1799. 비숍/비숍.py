# 1799_비숍
import sys
input = sys.stdin.readline

def dfs(n, s, lst):
    global ans
    if ans >= n + len(lst) - s:
        return
    ans = max(ans, n)
    for k in range(s, len(lst)):
        i, j = lst[k]
        if not used1[i + j] and not used2[i - j]:
            used1[i + j] = 1
            used2[i - j] = 1
            dfs(n + 1, k + 1, lst)
            used1[i + j] = 0
            used2[i - j] = 0

N = int(input()) # 체스판의 크기
arr = [list(map(int,input().split())) for _ in range(N)]
B_lst = []
W_lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if (i + j) % 2 == 0:
                B_lst.append((i, j))
            else:
                W_lst.append((i, j))

used1 = [0] * (N*2-1) # i + j 우상향
used2 = [0] * (N*2-1) # i - j 우하향
ans = 0
dfs(0, 0, B_lst)
res = ans
ans = 0
dfs(0, 0, W_lst)
print(res + ans)