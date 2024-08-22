"""
1번 선수는 4번 타자
각장 고득점인 타순을 찾고 그때의 득점을 출력

1: 안타
2: 2루타
3: 3루타
4: 홈런
0: 아웃

타석, 1루, 2루, 3루, 홈

이닝이 시작될 때 주자는 없음
이닝이 종료되는 시점은 3아웃이 발생한 시점
타순은 이닝이 종료되어도 첫 순로 갱신되지 않고 마지막 순서 다음 순부터 진행됨

타순을 만드는 dfs를 사용해서 모든 경우를 브루트포스로 탐색
타순이 만들어지면 그 상태에서 경기를 시뮬해보고 득점 계산

19:46 : 시간 초과. 게임 시뮬레이션이 시간을 오래 잡아먹음.. 더 효율적인 방법을 찾아야

타순을 그리디하게 찾아야 할까? (에반데)
게임 시뮬을 더 빠르게 만드는 게 더 가망 있지 않을까?
"""

import sys
input = sys.stdin.readline


def dfs(t, taja):
    global ans
    if t == 3:
        dfs(t + 1, taja + [0])
        return
    if t == 9:  # 타순 완성
        # 게임 진행
        score = 0
        taja_i = 0
        for ening in enings:  # 이닝 시작
            out = 0
            b1 = b2 = b3 = 0  # 1루, 2루, 3루
            b0 = 1
            while out < 3:  # 타순 돌아가는 중
                res = ening[taja[taja_i % 9]]  # 타자 결과
                if res == 4:
                    score += b0 + b1 + b2 + b3
                    b1 = b2 = b3 = 0
                elif res == 3:
                    score += b1 + b2 + b3
                    b1 = b2 = 0
                    b3 = 1
                elif res == 2:
                    score += b2 + b3
                    b3 = b1
                    b1 = 0
                    b2 = 1
                elif res == 1:
                    score += b3
                    b3 = b2
                    b2 = b1
                    b1 = 1
                else:  # 아웃인 경우
                    out += 1
                taja_i += 1
        # 모든 이닝 종료 후
        ans = max(ans, score)
        return

    for i in range(1, 9):
        if not used[i]:
            used[i] = 1
            dfs(t + 1, taja + [i])
            used[i] = 0


N = int(input())  # 이닝 수
enings = []
for _ in range(N):
    enings.append(list(map(int, input().split())))  # 각 이닝마다 각 선수가 얻는 결과 저장

used = [0] * 9
used[0] = 1
ans = 0
dfs(0, [])
print(ans)