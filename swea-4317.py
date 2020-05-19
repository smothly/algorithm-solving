'''
swea 4317번 칩 생산
링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWL21nCaM8wDFAUE
풀이 방법
- 
'''


def chip(i, j):
    global MAP
    global visited

    
    # 칩을 생산 할 수 있으면
    if MAP[i+1][j] == 0 and MAP[i][j+1] == 0 and MAP[i+1][j+1] == 0:
        MAP[i][j] = 1
        MAP[i+1][j] = 1
        MAP[i][j+1] = 1
        MAP[i+1][j+1] = 1
        # print(i, j, MAP)
        # visited[i][j] = True
        # visited[i+1][j] = True
        # visited[i][j+1] = True
        # visited[i+1][j+1] = True
        return 1
    else:
        return 0




import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 입력 받기
    H, W = map(int, input().split())
    MAP = [list(map(int, input().split())) for x in range(H)]
    visited = [[False] * W for _ in range(H)]

    answer = 0
    for i in range(H - 1):
        for j in range(W - 1):
            if MAP[i][j] == 0 and not visited[i][j]:
                answer += chip(i, j)            
    print('#{} {}'.format(test_case, answer))

    # break


'''
def is_markable(y,x):
    if y >= 0 and y < H -1 and x >= 0 and x < W -1:
        if board[y][x] == 0 and board[y+1][x] == 0 and board[y][x+1] == 0 and board[y+1][x+1] == 0:
            return True
        else:
            return False
    else:
        return False
 
 
def mark(y,x, val):
    board[y][x] = val
    board[y][x+1] = val
    board[y+1][x] = val
    board[y+1][x+1] = val
 
def dfs(y, x, cnt):
 
    global ans
    # 가로 마지막
    if x == W:
        if cnt > ans:
            ans = cnt
        return
    
    # 세로마지막
    if y == H:
        dfs(0, x+1, cnt)
        return
    
    # 
    if y == 0:
        bit = 0
        for yi in range(H):
            if board[yi][x] == 1:
                bit += 2 ** yi
 
        if memi[x][bit] >= cnt:
            return
        else:
            memi[x][bit] = cnt
 
    if is_markable(y,x):
        mark(y,x,1)
        dfs(y+1,x,cnt+1)
        mark(y,x,0)
 
    dfs(y+1, x, cnt)
 
 
 
 
T = int(input())
for tc in range(T):
    H, W = map(int,input().split())
    # 인풋
    board = [ list(map(int,input().split())) for _ in range(H) ]

    # ?? -1로 w x 1024를 채움
    memi = [[-1 for _ in range(2**10)] for _ in range(W)] # W x 1024
 
    ans = 0
 
    dfs(0,0,0)
 
    print("#"+str(tc+1),ans)
'''