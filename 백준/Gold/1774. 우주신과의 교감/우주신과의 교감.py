# 크루스칼
# 간선 중심

"""
15 3
5 1
1 1
9 17
5 2
1 9
9 5
1 14
13 11
1 11
5 14
15 9
11 17
9 9
11 1
18 4
9 15
1 2
5 4
output:37.77
"""

import math
def find(i):
    if p[i] != i:
        p[i] = find(p[i])
    return p[i]

def union(i, j):
    pi = find(i)
    pj = find(j)
    if pi < pj:
        p[pj] = pi
    else:
        p[pi] = pj

def distance(tup1, tup2):
    x1, y1 = tup1
    x2, y2 = tup2
    # return math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
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
    if find(i) != find(j):
        cost += dis
        num += 1
        union(i, j)

print(f'{cost:.2f}')