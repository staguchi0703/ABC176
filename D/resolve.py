def resolve():
    '''
    code here
    '''
    import collections

    H, W = [int(item) for item in input().split()]
    Ch, Cw = [int(item)-1 for item in input().split()]
    Dh, Dw = [int(item)-1 for item in input().split()]
    grid = [[item for item in input()] for _ in range(H)]
    max_num = 10**6
    fp = [[max_num for _ in range(W)] for _ in range(H)]
    
    que = collections.deque([[Ch, Cw, 0]])
    fp[Ch][Cw] = 0
    next_y_x = []
    for i in range(5):
        for j in range(5):
            next_y_x.append([-2 + i, -2 + j])
    next_y_x.remove([0,0])

    while que:
        y, x, w_num = que.popleft()

        for dy, dx in next_y_x:
            ny = y + dy
            nx = x + dx

            if 0 <= ny <= H-1 and 0 <= nx <= W-1:
                if abs(dy) + abs(dx) == 1:
                    if grid[ny][nx] == '.' and fp[ny][nx] > w_num:
                        que.appendleft([ny, nx, w_num])
                        fp[ny][nx] = w_num
                else:
                    nw = w_num +1
                    if grid[ny][nx] == '.' and fp[ny][nx] > nw:
                        que.append([ny, nx, nw])
                        fp[ny][nx] = nw

    if fp[Dh][Dw] != max_num:
        print(fp[Dh][Dw])
    else:
        print(-1)

if __name__ == "__main__":
    resolve()
