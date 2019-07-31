
def music(rx,ry,x,y):       # 받아오는 왼손 좌표값
    num1 = 0
    num2 = 7
    for i in range(rx, rx+18, 3):
        num1 += 1
        num2 += 1
        if(x >= rx-7) & (x <= rx-3):        # 높은음
            if(y >= i-1) & (y <= i+1):
                return num1
        elif(x >= rx-12) & (x <= rx-8):     # 낮은음
            if(y >= i-1) & (y <= i+1):
                return num2
