def solution(n, k, cmd):
    arr = [0] * n # [a,b] => a 는 위에 연결된 칸을 가리킴. b는 아래에 연결된 칸을 가리킴.. 이렇게 하면 되나?
    arr[0] = ['C', 1]
    arr[n-1] = [n-2, 'F']
    deleted = [] # 삭제된 행 번호 저장 배열
    state = [1] * n # 각 행의 상태 표시 (삭제됐나0 안 삭제됐나1)
    for i in range(1, n-1):
        arr[i] = [i-1, i+1]

    for cm in cmd:
        cm = cm.split()
        if len(cm) == 2:
            c = cm[0]
            X = int(cm[1])
            if c == "U": # X 칸 위 행 선택
                for _ in range(X):
                    if arr[k][0] != 'C':
                        k = arr[k][0]
            else: # X 칸 아래 행 선택
                for _ in range(X):
                    if arr[k][1] != 'F':
                        k = arr[k][1]

        else:
            if cm[0] == 'C': # 선택된 행 삭제 후 바로 아래 행 선택(마지막 행일 시 바로 윗 행 선택)
                state[k] = 0
                deleted.append(k)
                upper = arr[k][0]
                lower = arr[k][1]
                if upper != 'C':
                    arr[upper][1] = lower
                if lower != 'F':
                    arr[lower][0] = upper
                    k = lower
                else:
                    k = upper

            else: # 가장 최근에 삭제된 행을 원래대로 복구.. 가장 최근에 삭제된 것부터??!!
                rk = deleted.pop()
                state[rk] = 1
                upper = arr[rk][0]
                lower = arr[rk][1]
                if upper != 'C':
                    arr[upper][1] = rk
                if lower != 'F':
                    arr[lower][0] = rk

    for si in range(n):
        if state[si]:
            state[si] = 'O'
        else:
            state[si] = 'X'

    return ''.join(state)
