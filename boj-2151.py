'''
백준 2151번 거울 설치
링크: https://www.acmicpc.net/problem/2151
풀이 방법
-
'''


from collections import deque
direction = ((-1, 0), (1, 0), (0, -1), (0, 1)) # ^ > v < 순
def move(x, y, z):
    # 맵의 범위안에 있고 벽이 아니면
    if 0 <= x < N and 0 <= y < N and dist[x][y][z] != '*':
        return True
    else:
        return False


def bfs():
    while queue:
        x, y, z = queue.popleft()
        # 끝나는 조건
        if x == ex and y == ey:
            print(dist[x][y][z])
            return

        move_x = x + direction[z][0]
        move_y = y + direction[z][1]

        # 이동 가능한 곳이면 같은 방향으로 계속 이동
        while move(move_x, move_y, z) and room[move_x][move_y] == '.':
            move_x = move_x + direction[z][0]
            move_y = move_y + direction[z][1]

        # 거울을 놓을 수 있으면
        # 1. 이동방향과 같은 좌표
        # 2. 90도로 꺾는 좌표 ex) ^ -> >
        # 3. -90도로 꺽는 좌표 ex) ^ -> <
        if move(move_x, move_y, z) and room[move_x][move_y] == '!':
            # 1번 케이스 거울 횟수 증가 x
            dist[move_x][move_y][z] = dist[x][y][z]
            queue.append((move_x, move_y, z))

            if z < 2:
                k = 2
            else:
                k = 0
            # 90 도로 꺽는 2, 3 케이스
            for i in range(k, k+2):
                # 방문 되지 않은 곳이면
                if dist[move_x][move_y][i] == -1:
                    # 거울 횟수 1을 증가시켜 저장
                    dist[move_x][move_y][i] = dist[x][y][z]+1
                    queue.append((move_x, move_y, i))




import sys
# sys.stdin = open("input.txt", "r")

N = int(input())
room = [list(input().strip()) for i in range(N)]
# 방문 체크와 방향 거울 횟수
dist = [[[-1]*4 for _ in range(N)] for _ in range(N)]

ex, ey = 0, 0 # 끝나는 점
queue = deque()
for i in range(N):
    for j in range(N):
        if room[i][j] == '#':
            # 출발지
            if not queue:
                for k in range(4):
                    queue.append((i, j, k))
                    dist[i][j][k] = 0
            # 도착지
            else:
                ex, ey = i, j
            # 둘다 거울로 변경
            room[i][j] = '!'

bfs()

# 다른사람 풀이
# 숏코딩

import sys
sys.stdin = open("input.txt", "r")
n = int(input())
board = [input() for __ in range(n)]
D = '#'
M = '!'
B = '*'
E = '.'

# 출발지 뽑기
d0, d1 = (
    (r, c)
    for r in range(n)
    for c in range(n)
    if board[r][c] == D
)

print(d0, d1)
visited = [[False] * n for __ in range(n)]

q = [d0]
visited[d0[0]][d0[1]] = True
res = -1

while not visited[d1[0]][d1[1]]:
    res += 1
    nq = []
    for r, c in q:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            while 0 <= nr < n > nc >= 0 and board[nr][nc] != B:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    if board[nr][nc] == M:
                        nq.append((nr, nc))
                nr += dr
                nc += dc
    q = nq

print(res)


                
            
