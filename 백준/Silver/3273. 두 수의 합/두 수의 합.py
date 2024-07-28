N = int(input())
arr = list(map(int,input().split()))
arr.sort()
X = int(input())
ans = 0
i = 0
j = N-1
while i < j:
    res = arr[i] + arr[j]
    if res > X:
        j -= 1
    elif res < X:
        i += 1
    else:
        ans += 1
        i += 1
        j -= 1

print(ans)