'''
프로그래머스 게임 맵 최단 거리
링크: https://programmers.co.kr/learn/courses/30/lessons/1844
풀이방법
- BFS
- visit를 {x, y: cost} 형식으로 체크 해줘야 함
- 기존에 방문하지 않았거나 cost가 적을 경우만 추가
'''

from collections import deque

direction = ((-1, 0), (1, 0), (0, -1), (0, 1)) # ^ > v < 순

def solution(maps):
    
    # (x, y): cost 형식으로 방문관리
    visited = {(0, 0): 0}
    # 정답 초기 변수
    answer = float('inf')
    
    # (x, y, cost) 형식으로 큐에 들어감
    queue = deque()
    queue.append([0, 0, 1])

    # 맵의 끝 변수
    x_lim = len(maps)
    y_lim = len(maps[0])
    
    while queue:
        
        x, y, cost = queue.popleft()
        
        # 4가지 방향 탐색
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            
            # 맵안에 있고 벽이 아닌 경우
            if 0 <= nx < x_lim and 0 <= ny < y_lim and maps[nx][ny]:
                
                new_cost = cost + 1
                
                # 목적지에 도달하였을 경우
                if nx == lim_x - 1 and ny == lim_y - 1:
                    answer = min(answer, new_cost)
                
                # 방문을 하지 않았거나 / 방문한 곳의 new_cost가 기존보다 작을 경우
                elif visited.get((nx, ny)) == None or visited.get((nx, ny)) > new_cost:
                    # 방문 체크 해주고 다음 queue에 추가
                    visited[(nx, ny)] = new_cost
                    queue.append([nx, ny, new_cost])
    
    # 도착 못했을 경우
    if answer == float('inf'): answer =  -1
        
    return answer