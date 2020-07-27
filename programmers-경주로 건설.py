'''
프로그래머스 경주로 건설 2020 카카오 인턴십
링크: https://programmers.co.kr/learn/courses/30/lessons/67259
풀이방법
- BFS
- visit를 x, y, direction으로 체크 해줘야 함
- 진행방향이면 100 수직이면 600 추가해줘야함
- 기존에 방문하지 않았거나 cost가 적을 경우만 추가
'''

from collections import deque
# < v > ^ 순
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
def solution(board):

    # 직선도로:100 / 코너:500
    n = len(board)
    answer = float('inf')
    queue = deque()
    
    queue.append((0, 0, -1, 0)) # 처음 시작
    visit = {(0, 0, 0): 0, (0, 0, 1): 0, (0, 0, 2): 0, (0, 0, 3): 0}
    while queue:
        x, y, _dir, cost = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 맵 안에 있고 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                newcost = cost
                # 1. 시작일 경우
                if _dir == -1:
                    newcost += 100
                # 2. 진행방향이 평행일 경우
                elif (_dir - d) % 2 == 0:
                    newcost += 100
                # 3. 진행방향이 수직일 경우
                else:
                    newcost += 600
                
                # 목적지에 도달하였을 경우
                if nx == n-1 and ny == n-1:
                    answer = min(answer, newcost)
                # 기존에 방문하지 않았거나 / cost가 기존보다 적을경우만 queue에 append
                elif visit.get((nx, ny, d)) == None or visit.get((nx, ny, d)) > newcost:
                    visit[(nx, ny, d)] = newcost
                    queue.append((nx, ny, d, newcost))
    
    return answer