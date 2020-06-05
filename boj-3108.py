'''
백준 3108번 로고
링크: https://www.acmicpc.net/problem/3108
풀이방법
- 음수의 입력을 어떻게 처리하는지 보여줌
- bfs
'''

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    c[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2000 and 0 <= ny <= 2000:
                if a[nx][ny] == 1 and c[nx][ny] == 0:
                    c[nx][ny] = 1
                    q.append([nx, ny])

import sys
# sys.stdin = open("input.txt", "r")

from collections import deque
# 입력
N = int(input())
# -500 ~ 500 사이라 0 ~ 1000 -> 0 ~ 2000으로 만들어준다.
a = [[0]*2001 for _ in range(2001)]
c = [[0]*2001 for _ in range(2001)]

start = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 500; y1 += 500; x2 += 500; y2 += 500
    x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2
    start.append([x1, y1])
    # 직사각형 그리기
    for i in range(x1, x2+1):
        if i == x1 or i == x2:
            for j in range(y1, y2+1):
                a[i][j] = 1
        else:
            a[i][y1] = 1
            a[i][y2] = 1

q = deque()
answer = 0
for i in range(len(start)):
    x, y = start[i]
    if c[x][y] == 0:
        bfs(x, y)
        answer += 1

# 입력부분에 1이 있으면 연필 내리고 시작한거
if a[1000][1000] == 1:
    answer -= 1

print(answer)


