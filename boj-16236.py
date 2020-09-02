'''
백준 16236번 아기 상어
링크: https://www.acmicpc.net/problem/16236
풀이방법
- BFS
- heapq를 사용
- 조건을 잘 따져야 하는 문제앋.
- 출처: https://rebas.kr/714
'''

import sys
from heapq import heappush, heappop

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
def bfs(distance, x, y):

    # 초기 아기상어
    size = 2 # 크기
    up = 0 # 먹은 횟수
    answer = 0 # 정답

    queue = []
    # heapq를 사용해서 거리순 x(위쪽) y(왼쪽) 순으로 정렬하면서 추가
    heappush(queue, (distance, x, y))
    visited = [[False] * N for _ in range(N)]

    while queue:
        
        distance, x, y = heappop(queue)

        # 먹을 수 있으면
        if 0 < MAP[x][y] < size:
            up += 1
            MAP[x][y] = 0
            # 다 먹었을 경우 크기 1개 증가 후 초기화
            if up == size:
                size += 1
                up = 0
            # 정답에 거리만큼 추가 후 초기화
            answer += distance
            distance = 0
            # 나머지 큐들 초기화
            while queue:
                print("초기화")
                queue.pop()
            # 방문 배열 초기화
            visited = [[False] * N for _ in range(N)]

        # 4 방향 탐색
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            # 맵 안에 있고 지나갈 수 있으면(물고기의 크기 <= 상어의 크기)
            # 방문하지 않았을 경우
            if 0 <= nx < N and 0 <= ny < N and MAP[nx][ny] <= size\
                and not visited[nx][ny]:
                visited[nx][ny] = True
                heappush(queue, (distance + 1, nx, ny))
    
    print(answer)

sys.stdin = open("input.txt", "r")

# N, M 입력 
N = int(sys.stdin.readline())

MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            MAP[i][j] = 0
            bfs(0, i, j) # 거리, x, y
