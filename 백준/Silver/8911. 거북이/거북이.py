""""
(0,0) 에서 북쪽 facing으로 출발.
가장 낮고 큰 열과 가장 낮고 큰 행을 알아내야 함
"""


dir = [(-1,0),(0,-1),(1,0),(0,1)] # 상 좌 하 우 # 왼쪽 90도 회전은 - 1, 오른쪽 90도 회전은 + 1

T = int(input())
for tc in range(T):
    cmd = input()
    
    # arr = [[0] * 1001 for _ in range(1001)]
    
    face = 0
    i, j = 0, 0
    min_n = 0
    max_n = 0
    min_m = 0
    max_m = 0

    for c in cmd:
        if c == 'F':
            di, dj = dir[face]
            i += di
            j += dj
            min_n = min(min_n, i)
            max_n = max(max_n, i)
            min_m = min(min_m, j)
            max_m = max(max_m, j)
            
        elif c == 'B':
            di, dj = dir[(face + 2) % 4]
            i += di
            j += dj
            min_n = min(min_n, i)
            max_n = max(max_n, i)
            min_m = min(min_m, j)
            max_m = max(max_m, j)
            
        elif c == 'L':
            face = (face - 1)%4
        else: # c == 'R'
            face = (face + 1)%4
    
    print(abs(max_n - min_n) * abs(max_m - min_m))
    
    