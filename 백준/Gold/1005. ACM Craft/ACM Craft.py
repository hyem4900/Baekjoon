import sys
input=sys.stdin.readline
from copy import deepcopy

def func():
    while [0] in need.values():
        for i,j in need.items():
            if j == [0]:
                need[i] = []
                for p,q in need.items():
                    if i in q:
                        q.remove(i)
                        times[p] = max(times[p],times_original[p] + times[i])


T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split()) # 건물 개수 N, 건설 규칙 K
    times = [0] + list(map(int, input().split()))
    times_original = deepcopy(times)
    need = {}
    for _ in range(1,N+1):
        need[_] = [0]
    for _ in range(K):
        X,Y = map(int,input().split())
        need[Y].append(X)  # need = {1: [0], 2: [0, 1], 3: [0, 1], 4: [0, 2, 3]}
    W = int(input()) # 건설해야 할 건물 번호
    func()
    print(times[W])