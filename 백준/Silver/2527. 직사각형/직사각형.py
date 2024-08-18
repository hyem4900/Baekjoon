for n in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int,input().split())
    if x1 > x3:
        x1,y1,x2,y2,x3,y3,x4,y4 = x3,y3,x4,y4,x1,y1,x2,y2
    # case d (공통X)
    if y2 < y3 or y1 > y4 or x2 < x3:
        print("d")
    # case c (점)
    elif (x2, y1) == (x3, y4) or (x2,y2) == (x3,y3):
        print("c")
    # case b (선분)
    elif x2 == x3 or y1 == y4 or y2 == y3:
        print("b")
    else:
        print("a")