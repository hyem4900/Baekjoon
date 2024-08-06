# 1799_비숍
import sys
input = sys.stdin.readline

def B_dfs(n, s):
    global B_ans
    if B_ans >= n + len(B_lst) - s:
        return
    B_ans = max(B_ans, n)
    for k in range(s, len(B_lst)):
        i, j = B_lst[k]
        if not B_used1[i + j] and not B_used2[i - j]:
            B_used1[i + j] = 1
            B_used2[i - j] = 1
            B_dfs(n + 1, k + 1)
            B_used1[i + j] = 0
            B_used2[i - j] = 0

def W_dfs(n, s):
    global W_ans
    if W_ans >= n + len(W_lst) - s:
        return
    W_ans = max(W_ans, n)
    for k in range(s, len(W_lst)):
        i, j = W_lst[k]
        if not W_used1[i + j] and not W_used2[i - j]:
            W_used1[i + j] = 1
            W_used2[i - j] = 1
            W_dfs(n + 1, k + 1)
            W_used1[i + j] = 0
            W_used2[i - j] = 0

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

B_used1 = [0] * (N*2-1) # i + j 우상향
B_used2 = [0] * (N*2-1) # i - j 우하향
W_used1 = [0] * (N*2-1)
W_used2 = [0] * (N*2-1)
B_ans = 0
W_ans = 0
B_dfs(0, 0)
W_dfs(0, 0)

print(B_ans + W_ans)