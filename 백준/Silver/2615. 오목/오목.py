import sys
input = sys.stdin.readline

arr = [list(map(int,input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        for w in [1,2]:
            if arr[i][j] == w:
                # 가로
                for k in range(5):
                    if j+k>=19 or arr[i][j+k] != w:
                        break
                else:
                    if (j+5 >= 19 or arr[i][j+5] != w) and (j-1<0 or arr[i][j-1] != w):
                        print(w)
                        print(i+1,j+1)
                        exit()
                 
                # 세로
                for k in range(5):
                    if i+k >= 19 or arr[i+k][j] != w:
                        break
                else:
                    if (i+5 >= 19 or arr[i+5][j] != w) and (i-1 < 0 or arr[i-1][j] != w):
                        print(w)
                        print(i+1, j+1)
                        exit()
            
                # 우상향
                for k in range(5):
                    if i-k not in range(19) or j+k not in range(19) or arr[i - k][j + k] != w:
                        break
                else:
                    if (i-5 < 0 or j+5 >= 19 or arr[i-5][j+5] != w) and (i+1 >= 19 or j-1 <0 or arr[i+1][j-1] != w):
                        print(w)
                        print(i+1,j+1)
                        exit()
                # 우하향
                for k in range(5):
                    if i+k not in range(19) or j+k not in range(19) or arr[i + k][j + k] != w:
                        break
                else:
                    if (i+5 >= 19 or j+5 >= 19 or arr[i+5][j+5] != w) and (i-1 < 0 or j-1<0 or arr[i-1][j-1] != w):
                        print(w)
                        print(i+1,j+1)
                        exit()

print(0)