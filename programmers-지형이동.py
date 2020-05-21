'''
링크: https://programmers.co.kr/learn/courses/30/lessons/62050
풀이방법
- BFS로 각 지형 group을 구한다.
- 다른 지형으로 가는 edge들을 구한다
- edge들을 크루스칼 알고리즘으로 Minimum Spanning Tree를 찾는다.
'''

from collections import deque

direction = ((1, 0), (0, 1), (-1, 0), (0, -1)) # ^ > v < 순
def bfs(land, x, y, height, group):
    
    grouping[x][y] = group
    queue = deque([(x, y)])
    _min, _max = land[x][y], land[x][y]
    
    while queue:
        qx, qy = queue.popleft()
        # 4방향 방문
        for d in direction:
            move_x = qx + d[0]
            move_y = qy + d[1]
            # 맵 안에 있고, height보다 작을경우
            if 0 <= move_x < l_len and 0 <= move_y < l_len and \
                abs(land[move_x][move_y] - land[qx][qy]) <= height and \
                grouping[move_x][move_y] == 0 :
                grouping[move_x][move_y] = group
                queue.append([move_x, move_y])

    return    

# 크루스칼 알고리즘    
parent = {}
rank = {}

# 정점을 독립적인 집합으로 만든다.
def make_set(v):
    parent[v] = v
    rank[v] = 0

# 해당 정점의 최상위 정점을 찾는다.
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
        
    return parent[v]

# 두 정점을 연결한다.
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:
        # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def solution(land, height):
    
    answer = 0
    global l_len
    l_len = len(land)
    global grouping
    grouping = [[0] * l_len for _ in range(l_len)]
    
    # 각 지형을 그룹 짓기
    group = 0
    for i in range(l_len):
        for j in range(l_len):
            if grouping[i][j] == 0:
                group += 1
                bfs(land, i, j, height, group)
    
    # 그룹이 다를경우 이을 수 있는 간선들 구하기    
    edges=[]
    for i in range(l_len):
        for j in range(l_len):
            for d in direction:
                move_x = i + d[0]
                move_y = j + d[1]
                # 맵을 벗어나지 않고, 서로 다른 지역일 경우
                if 0<=move_x<l_len and 0<=move_y<l_len and grouping[i][j] != grouping[move_x][move_y]:
                    # weight, u, v 추가
                    edges.append([abs(land[i][j]-land[move_x][move_y]),grouping[i][j],grouping[move_x][move_y]])
    
                
    # 여기서 부터는 크루스칼 알고리즘
    edges.sort() # edge 가중치 순으로 정렬
    # 초기화
    for i in range(1, group+1):
        make_set(i)
    
    mst = []
    for edge in edges:
        w, u, v = edge
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    
    return  sum(map(lambda x: x[0], mst))