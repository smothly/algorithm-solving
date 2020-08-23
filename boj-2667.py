
'''
백준 2667번 단지 번호 붙이기
링크: https://www.acmicpc.net/problem/2667
풀이방법
- DFS
'''


from sys import stdin
from collections import deque
stdin = open("input.txt", "r")

# 방향: ^ > v <
direction = ((0, 1), (1, 0), (0, -1), (-1, 0)) 

def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    count = 1

    while queue:

        x, y = queue.popleft()
    
        # 4가지 방향 전부 탐색
        for d in direction:
            move_x = x + d[0]
            move_y = y + d[1]
            # 맵에 있고 방문되지 않고 집이면
            if 0 <= move_x < N and 0 <= move_y < N and \
                not visited[move_x][move_y] and MAP[move_x][move_y] == 1:
                queue.append((move_x, move_y))
                # 방문 체크하고 큐에 추가
                visited[move_x][move_y] = True
                count += 1

    return count

# N: 지도의 크기
N = int(stdin.readline())
# 2차원 배열로 입력받기
MAP = [list(map(int, stdin.readline().strip())) for _ in range(N)]
# 방문 체크 배열
visited = [[False] * N for _ in range(N)]

apart = []
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1 and not visited[i][j]:
            apart.append(bfs(i, j))
            
# 오름차순 정렬
apart.sort()
# 아파트 개수 출력
print(len(apart))
for a in apart:
    print(a)
