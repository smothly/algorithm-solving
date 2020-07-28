'''
링크: https://programmers.co.kr/learn/courses/30/lessons/67260
풀이방법
- DFS
- 정답을 보고 풀었다..
- dfs를 할때 선방문노드가 있는 노드를 방문하면 체크한 다음에
  선방문 노드를 방문하고 바로 체크했던 노드로 가는게 핵심이다.
'''

import sys
sys.setrecursionlimit(10**9)

def dfs(v):
    if check[v]:
        return
    if not check[prev_visit[v]]:
        next_visit[prev_visit[v]] = v
        return
    check[v] = 1
    if next_visit[v]:
        dfs(next_visit[v])
    for i in graph[v]:
        dfs(i)


def solution(n, path, order):
    global N, graph, prev_visit, check, next_visit
    
    N = n
    start_room = 0
    num_of_room = 0
    
    # 그래프를 저장하는 배열
    graph = [[] for _ in range(N)]
    # 선방문해야 하는 방을 저장하는 배열, prev_visit[후방문방] = 선방문방
    prev_visit = [0 for _ in range(N)]
    # 그래프의 노드 방문여부를 저장하는 배열
    check = [0 for _ in range(N)]
    # 후방문해야 하는 방을 저장하는 배열, next_visit[선방문방] = 후방문방
    next_visit = [0 for _ in range(N)]
    
    # 양방향 그래프
    for room_A, room_B in path:
        graph[room_A].append(room_B)
        graph[room_B].append(room_A)
    
    # 선 방문 그래프
    for room_A, room_B in order:
        prev_visit[room_B] = room_A
    
    # 시작 지점보다 선 방문이 있다면
    if prev_visit[start_room]:
        return False
    
    check[start_room] = 1
    for i in graph[start_room]:
        dfs(i)
    
    for i in range(N):
        if check[i]:
            num_of_room += 1

    return True if num_of_room == N else False