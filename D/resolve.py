def resolve():
    '''
    code here
    '''
    import collections

    H, W = [int(item) for item in input().split()]
    Ch, Cw = [int(item)-1 for item in input().split()]
    Dh, Dw = [int(item)-1 for item in input().split()]
    grid = [[item for item in input()] for _ in range(H)]

    fp = [[10**6 for _ in range(W)] for _ in range(H)]

    que = collections.deque([[Ch, Cw, 0]])
    fp[Ch][Cw] = 0
    next_y_x = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    w_goto = []
    for i in range(5):
        for j in range(5):
            if [i, j] in next_y_x:
                pass
            else:
                w_goto.append([-2 + i, -2 + j])
    w_goto.remove([0,0])

    while que:
        temp = que.popleft()
        w_num = temp[2]

        for dy, dx in next_y_x:
            ny = temp[0] + dy
            nx = temp[1] + dx

            if 0 <= ny <= H-1 and 0 <= nx <= W-1:
                if grid[ny][nx] == '.' and fp[ny][nx] > w_num:
                    que.append([ny, nx, temp[2]])
                    fp[ny][nx] = w_num
        
        cnt = 0
        for dy, dx in w_goto:
            nwy = temp[0] + dy
            nwx = temp[1] + dx
            nw = w_num +1

            if 0 <= nwy <= H-1 and 0 <= nwx <= W-1 and cnt <= 3:
                if grid[nwy][nwx] == '.' and fp[nwy][nwx] > w_num:
                    que.append([nwy, nwx, nw])
                    fp[nwy][nwx] = nw
                    cnt += 1

    if fp[Dh][Dw] != 10**6:
        print(fp[Dh][Dw])
    else:
        print(-1)

if __name__ == "__main__":
    resolve()
