'''
백준 2636번 치즈
링크: https://www.acmicpc.net/problem/2636
풀이방법
- bfs
- 핵심은 입력을 2칸씩 더받아서 초기화 해주는 것
- 구멍을 계산하는 게 아니라 공기 기준으로 bfs를 할 것
'''

from collections import deque
direction = ((1, 0), (0, 1), (-1, 0), (0, -1)) # ^ > v < 순

def bfs(x, y):
    time = 0
    count = 0

    while True:
        cheese = []
        queue = deque([(x, y)])
        while queue:
            qx, qy = queue.popleft()

            for d in direction:
                move_x = qx + d[0]
                move_y = qy + d[1]
                if 0 <= move_x < N+2 and 0 <= move_y < M+2:
                    # 공기
                    if MAP[move_x][move_y] == 0:
                        MAP[move_x][move_y] = -1
                        queue.append((move_x, move_y))
                    # 구멍이 아닌 치즈
                    elif MAP[move_x][move_y] == 1:
                        MAP[move_x][move_y] = -1
                        cheese.append((move_x, move_y))
        if not cheese:
            break
        
        time += 1
        count = len(cheese)

        # 복원
        for i in range(N+2):
            for j in range(M+2):
                if MAP[i][j] == -1:
                    MAP[i][j] = 0

    print(time, count)

import sys
# sys.stdin = open("input.txt", "r")

# 입력
N, M = map(int, input().split())
MAP = [[0] * (M+2)] + [[0] + list(map(int, sys.stdin.readline().split())) + [0] for _ in range(N)] + [[0] * (M+2)]

bfs(0, 0)