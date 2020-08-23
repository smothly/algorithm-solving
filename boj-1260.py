'''
백준 1260번 DFS와 BFS
링크: https://www.acmicpc.net/problem/1260
풀이방법
- DFS / BFS 기본 문제
- DFS는 재귀로 BFS는 queue로 풀면 된다.
- 그래프를 인접 리스트로 표현하고 방문체크를 하며 순회하면 된다.
'''

def dfs(v):
    visited[v] = 1

    print(v, end= " ")
    # 다음 방문 노드 찾기
    for next_v in adj[v]:
        if not visited[next_v]:
            dfs(next_v)

def bfs(v):

    queue = []
    queue.append(v)
    visited[v] = True

    while queue:
        cur_v = queue.pop(0)
        print(cur_v, end=" ")
        # 다음 방문 노드 찾기
        for next_v in adj[cur_v]:
            if not visited[next_v]:
                queue.append(next_v)
                visited[next_v] = True


from sys import stdin
stdin = open("input.txt", "r")

# N: 정점의 개수
# M: 간선의 개수
# V: 시작 정점의 번호
N, M, V = map(int, stdin.readline().split())

# 인접 노드 갖고 있는 리스트 선언
adj = [[] for _ in range(N+1)]


for _ in range(M):
    # 간선 입력
    v1, v2 = map(int, stdin.readline().split())
    # 양방향이므로 두군데에 추가
    adj[v1].append(v2)
    adj[v2].append(v1)

# 정렬
for edges in adj:
    edges.sort()
    
# DFS
visited = [False] * (N+1)
dfs(V)
print()

# BFS
visited = [False] * (N+1)
bfs(V)
