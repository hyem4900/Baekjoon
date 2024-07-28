N = int(input())
arr = list(map(int,input().split()))
arr.sort()
mini = float("inf")
i = 0
j = N-1

while i < j:
    res = arr[i] + arr[j]
    if abs(res) < mini:
        mini = abs(res)
        a = arr[i]
        b = arr[j]
    if res > 0:
        j -= 1
    elif res < 0:
        i += 1
    else:
        a = arr[i]
        b = arr[j]
        break

print(a,b)