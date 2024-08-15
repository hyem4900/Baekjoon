import math
def find(i):
    if p[i] != i:
        p[i] = find(p[i])
    return p[i]

def union(i, j):
    p[find(i)] = find(j)

def distance(tup1, tup2):
    x1, y1 = tup1
    x2, y2 = tup2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

p = list(range(N+1))

m = 0
for _ in range(M):
    a, b = map(int, input().split())
    if find(a-1) != find(b-1):
        m += 1
        union(a-1, b-1)

gansuns = []
# 간선 구하기
for i in range(N-1):
    for j in range(i + 1, N):
        gansuns.append((distance(arr[i],arr[j]), i , j))

gansuns.sort()

num = m
cost = 0
for dis, i, j in gansuns:
    if num == N-1:
        break
    if find(i) != find(j):
        cost += dis
        num += 1
        union(i, j)

print(f'{cost:.2f}')