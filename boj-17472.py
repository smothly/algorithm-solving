'''
링크: https://www.acmicpc.net/problem/17472
풀이방법
- bfs를 통해 섬의 개수 파악
- 가로와 세로 한번 씩 탐색해서 만들 수 있는 간선 전부 구하기
- 최소신장트리 krusckal 알고리즘: https://debuglog.tistory.com/84
'''

from collections import deque

# 섬의 개수 체크하고 번호 매기기
direction = ((1, 0), (0, 1), (-1, 0), (0, -1)) # ^ > v < 순
def bfs(x, y, island_number):
    queue = deque([(x, y)])
    visited[x][y] = True
    MAP[x][y] = island_number

    while queue:
        qx, qy = queue.popleft()
        # 4방향 방문
        for i in range(4):
            move_x = qx + direction[i][0]
            move_y = qy + direction[i][1]
            # 지도안에 있고 방문 되지 않고 1일 경우
            if 0 <= move_x < N and 0 <= move_y < M and not visited[move_x][move_y] and MAP[move_x][move_y] == 1:
                visited[move_x][move_y] = True
                MAP[move_x][move_y] = island_number
                queue.append((move_x, move_y))
    
    return

import sys
# sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())

# 입력받기
MAP = [list(map(int, sys.stdin.readline().split())) for x in range(N)]

visited = [[False] * M for _ in range(N)]


island_number = 1

# 섬의 번호 매기는 과정 bfs
for i in range(N):
    for j in range(M):
        # 땅이고 방문되지 않으면
        if MAP[i][j] == 1 and not visited[i][j]:
            # island_info[island_number].append((i, j))
            bfs(i, j, island_number)
            island_number += 1

# 간선 정보를 담는다.
line = []
for i in range(N):
    for j in range(M-1):
        if MAP[i][j] != 0 and MAP[i][j+1] == 0: # 시작하는 부분
            for k in range(1, M-j):
                if MAP[i][j+k] != 0: # 끝나는 부분
                    if k-1>=2:
                        line.append((k-1, MAP[i][j], MAP[i][j+k]))
                    break

# 세로방향으로 만들어줌
MAP = list(zip(*MAP)) 
for i in range(M):
    for j in range(N-1):
        if MAP[i][j] != 0 and MAP[i][j+1] == 0: # 시작하는 부분
            for k in range(1, M-j):
                if MAP[i][j+k] != 0: # 끝나는 부분
                    if k-1>=2:
                        line.append((k-1, MAP[i][j], MAP[i][j+k]))
                    break
                
# 여기서 부터는 크루스칼 알고리즘
line.sort()

# 해당 정점의 최상위 정점을 찾는다.
def findParent(v):
    if parent[v] != v:
        parent[v] = findParent(parent[v])
        
    return parent[v]

# 두 정점을 연결한다.
def union(v, u):
    root1 = findParent(v)
    root2 = findParent(u)
    
    if root1 != root2:
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1
    return

rank = [0]*(island_number+1)
parent = list(range(0,island_number+1))
ans = 0
cnt = 0
for weight, v, u in line : ## x:간선값,y,z : 노드
    if findParent(v) != findParent(u) : ## 부모가 다르면
        cnt += 1 ## 간선연결
        ans += weight ## 간선값을 더한다
        union(v,u)
    if cnt == island_number-2 : ## 간선의 갯수는 노드-1
        print(ans)
        sys.exit()
print(-1)