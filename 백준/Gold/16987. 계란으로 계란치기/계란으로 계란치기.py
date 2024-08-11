def dfs(ci): # 현재 들고 있는 계란의 인덱스
    global ans
    if ci == N: # 여기서 정답 처리
        res = 0
        for a in arr:
            if a[0] <= 0:
                res += 1
        ans = max(ans, res)
        return

    curr_h, curr_w = arr[ci]
    if curr_h <= 0:
        dfs(ci + 1)
        return

    flag = 0
    for i in range(N):
        if arr[i][0] > 0 and i != ci: # 내구도가 남아 있으면
            arr[i][0] -= arr[ci][1]
            arr[ci][0] -= arr[i][1]
            dfs(ci + 1)
            arr[i][0] += arr[ci][1]
            arr[ci][0] += arr[i][1]
            flag = 1

    if not flag: # 들고 있는 계란 외 내구도 남아 있는 계란이 없음
        res = 0
        for a in arr:
            if a[0] <= 0:
                res += 1
        ans = max(ans, res)
        return

N = int(input())
arr = []
ans = 0
for _ in range(N):
    h, w = map(int,input().split()) # 내구도, 무게
    arr.append([h, w])

dfs(0)
print(ans)