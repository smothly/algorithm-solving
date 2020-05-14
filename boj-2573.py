'''
백준 2573번 빙산
링크: https://www.acmicpc.net/problem/2573
풀이방법
- deque를 이용
- bfs나 dfs는 완전 사고를 바꿔야 함 - 방문 관리 맵, 큐로 모든 방향 탐색
- bfs를 통해 빙산 개수 체크 + 녹여야 할 빙산 리턴
'''

from collections import deque
import sys

direction = ((1, 0), (0, 1), (-1, 0), (0, -1)) # ^ > v < 순
def bfs(x, y):
    rtn = []
    # 첫번째 지점을 큐에 넣음
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        qx, qy = queue.popleft()
        c = 0
        # 4방향 방문
        for i in range(4):
            move_x = qx + direction[i][0]
            move_y = qy + direction[i][1]
            # 지도안에 있고 방문 되지 않았으면
            if 0 <= move_x < N and 0 <= move_y < M and not visited[move_x][move_y]:
                # 0이면 -해주기
                if iceberg[move_x][move_y] == 0:
                    c += 1
                # 0이 아닐 경우 방문체크와 다음 큐로
                else:
                    visited[move_x][move_y] = True
                    queue.append((move_x, move_y))
        # 한 점마다 return해주어 녹이기 작업을 위함
        rtn.append((qx, qy, c))
    return rtn

# sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())

# 입력받기
iceberg = [list(map(int, sys.stdin.readline().split())) for x in range(N)]

year = 0
while True:
    # 방문 관리
    visited = [[False] * M for _ in range(N)]
    ice = deque()
    count = 0
    
    for x in range(N):
        for y in range(M):
            # 빙산이 있고 방문되지 않으면
            if iceberg[x][y] > 0 and not visited[x][y]:
                count += 1
                # 빙산 개수가 2개이상이면
                if count > 1:
                    print(year)
                    sys.exit()
                # ice가 방문할 수 있는 노드들
                ice.extend(bfs(x, y))
    # 2개로 나누어 지지 않으면
    if count == 0:
        year = 0
        break

    year += 1

    # queue에서 끄내서 얼음 녹이기
    while ice:
        x, y, v = ice.popleft()
        iceberg[x][y] = max(0, iceberg[x][y] - v)
print(year)