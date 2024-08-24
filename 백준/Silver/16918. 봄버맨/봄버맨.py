# 봄버맨
"""
맵 크기 NxM

폭탄이 있는 칸은 3초가 지난 후에 폭발
폭탄 터지면 그 칸이 빈칸이 되며, 인접한 네칸도 함께 파괴됨.
인접 칸에 폭탄 있는 경우 인접 폭탄은 폭발 없이 파괴됨. (연쇄 반응X)

봄버맨은 모든 칸 자유롭게 이동.
봄버맨의 행동
1. 초기에 일부 칸에 폭탄 설치해 놓음. 모든 폭탄이 설치된 시간은 같음
2. 1초 동안 행동X
-3. 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄 설치. 모든 폭탄이 설치된 시간은 같음
-4. 1초가 지난 후 3초 전에 설치된 폭탄이 모두 폭발
이렇게 3과 4를 반복

출력 결과 반복되는 패턴이 존재
짝수 초 -> 폭탄으로 꽉 차 있음
1보다 큰 홀수 초 -> 4초 텀으로 특정 패턴 반복 (총 두가지 패턴)
=> 5초까지만 패턴 파악하면 나머지 다 알 수 있음
"""

N, M, n = map(int, input().split()) # n초가 지난 후의 격자판 상태를 출력

arr = [list(input()) for _ in range(N)]

if n == 1:
    for ar in arr:
        print(*ar, sep='')
    exit()

# 초기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'O':
            arr[i][j] = 0

# 아무것도 하지 않고 1초 흐름
t = 1

# 3과 4를 반복
while True:
    t += 1
    # 1초 동안 폭탄이 설치돼 있지 않은 모든 칸에 폭탄을 설치함
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '.':  # 빈칸에 폭탄 설치
                arr[i][j] = t

    pattern_even = [ar[:] for ar in arr]

    # 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다
    t += 1
    bombs = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == t - 3:
                bombs.append((i, j))
    for bomb in bombs:
        i, j = bomb
        arr[i][j] = '.'
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                arr[ni][nj] = '.'

    if t == 3:
        pattern_odd1 = [ar[:] for ar in arr]
    if t == 5:
        pattern_odd2 = [ar[:] for ar in arr]
        break

if n % 2 == 0:
    # pattern_even
    for p in pattern_even:
        print(*map(lambda x: 'O' if x != '.' else x, p), sep='')
else: # 홀수
    if n % 4 == 1:
        for p in pattern_odd2:
            print(*map(lambda x: 'O' if x != '.' else x, p), sep='')
    else:
        for p in pattern_odd1:
            print(*map(lambda x: 'O' if x != '.' else x, p), sep='')