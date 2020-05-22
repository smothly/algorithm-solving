'''
백준 14502번 연구소
링크: https://www.acmicpc.net/problem/14502
풀이방법
- 벽을 세우는 모든 경우의 수를 가지고 bfs를 통해 max값을 찾아내면 된다.
- 벽을 세우는 경우의 수를  combination으로 작업하면 더 빨라짐
- 바이러스 위치도 기억해놨다가 실행하면 더 빨라짐
'''

from collections import deque
import copy


direction = ((1, 0), (0, 1), (-1, 0), (0, -1)) # ^ > v < 순
def bfs(MAP):
    global answer
    # 복사하고 바이러스 퍼뜨리기
    m = copy.deepcopy(MAP)
    queue = deque()
    
    # 큐에 추가
    for i in range(N):
        for j in range(M):
            if m[i][j] == 2:
                queue.append((i, j))
    
    # bfs 과정
    while queue:
        qx, qy = queue.popleft()
        for d in direction:
            move_x = qx + d[0]
            move_y = qy + d[1]
            if 0 <= move_x < N and 0 <= move_y < M and m[move_x][move_y] == 0:
                m[move_x][move_y] = 2
                queue.append((move_x, move_y))
    
    # 0인 개수 세고 answer 업데이트
    answer = max(answer, sum([r.count(0) for r in m]))



def wall(count):
    if count == 3:
        bfs(MAP)
        return
    # DFS를 통하여 벽을 추가하는 과정
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                MAP[i][j] = 1
                wall(count + 1)
                MAP[i][j] = 0 # reset

import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
answer = 0

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for x in range(N)]
wall(0)
print(answer)

