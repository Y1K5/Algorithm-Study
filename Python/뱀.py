import sys
from collections import deque

def playGame(n, board, cmd) :
    dr = [0, -1, 0, 1]      # 우, 상, 좌, 하
    dc = [1, 0, -1, 0]
    t = 0   # 시간
    head = 0    # 뱀의 머리 방향
    snake = deque()
    snake.appendleft([0, 0])
    board[0][0] = 1

    while (True) :
        t += 1
        nr = snake[0][0] + dr[head]
        nc = snake[0][1] + dc[head]

        #종료 조건: 뱀이 벽에 부딪힐때, 몸에 부딪힐 때
        if (nr<0 or nr>=n or nc<0 or nc>=n or board[nr][nc]==1) :
            break
        if(board[nr][nc] != 2) :
            x, y = snake.pop()
            board[x][y] = 0

        snake.appendleft([nr, nc])
        board[nr][nc] = 1

        if (cmd.get(t) == 'L') : 
            head = (head + 1) %4
        elif (cmd.get(t) == 'D') :
            head = (head + 3) %4

    return t

def solution(n, k, l, apple, rotation) :
    answer = 0
    board = [[0]*n for _ in range(n)]

    for i, j in apple :
        board[i-1][j-1] = 2
    
    cmd = dict(rotation)
    answer = playGame(n, board, cmd)

    return answer

if __name__ == "__main__" :
    # input = sys.stdin.readline

    N = int(input())
    K = int(input())

    apple = [list(map(int, input().split())) for _ in range(K)]

    L = int(input())
    rotation = []
    for _ in range(L):
        i, j = map(str, input().split())
        rotation.append([int(i), j])

    answer = solution(N, K, L, apple, rotation)

    print(answer)