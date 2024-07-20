import sys
input = sys.stdin.readline

def func(p):
    global result
    if p != erase:
        if tree[p] == [] or tree[p] == [erase]:
            result+=1
            return
        for c in tree[p]:
            func(c)

N = int(input())
arr = list(map(int,input().split()))
erase = int(input())
tree = {}
for i in range(N):
    tree[i] = []
for c,p in enumerate(arr):
    if p != -1:
        tree[p].append(c)
    else:
        start = c
result = 0
func(start)
print(result)