# from collections import deque

# def solution(ball, order):
#     answer = []
    
#     ball = deque(ball)
#     wait = deque()
    
#     for o in order:
#         print(o, ball, wait)
#         if ball[0] == o:
#             answer.append(ball.popleft())
#             # 끄내고 나서 
#             while ball[0] in wait:
#                 wait.remove(ball[0])
#                 answer.append(ball.popleft())
#         elif ball[-1] == o:
#             answer.append(ball.pop())
#             while ball[-1] in wait:
#                 wait.remove(ball[-1])
#                 answer.append(ball.pop())
#         else:
#             wait.append(o)
    
#     return answer

# solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3])


def solution(n):
    
    if n < 10:
        return [0, n]

    count = 0
    # 한자리수가 될 때까지
    while n >= 10:
        n = str(n)
        # 길이가 짝수일 경우
        # 나뉘는 경우의 수 1가지이다.
        if len(n) % 2 == 0:        
            div = len(n) // 2
            # 오른쪽에 숫자 0이 안나올때까지 (유효한 숫자가 아니므로)
            while div < len(n) - 1 and n[div] == '0':
                div += 1

            # 만약에 div가 끝까지 가고 오른쪽에 0밖에 없으면 ex) 980000
            # 왼쪽으로 재탐색
            if div == len(n) - 1 and n[div] == '0':
                div = len(n) // 2

                while n[div] == '0':
                    div -= 1

            # 숫자 업데이트
            n = int(n[:div]) + int(n[div:])
            count += 1
        
        # 홀수 일경우
        # 나뉘는 경우의 수가 2가지이다.  2가지중에 더 작은 수로
        else:
            # 왼쪽 기준
            left_div = len(n) // 2
            
            
            while n[left_div] == '0':
                left_div -= 1

            # 왼쪽에서 끝까지 갔는데 마지막 지점이거나 오른쪽 수가 0이 면
            if left_div == 0 or n[left_div+1] == 0:
                left = float('inf')
            else:
                left = int(n[:left_div]) + int(n[left_div:])

            # 오른쪽 기준
            right_div = (len(n) // 2 )+ 1
            print(right_div)
            while right_div < len(n) - 1 and n[right_div] == '0':
                right_div += 1

            if right_div == len(n) - 1 and n[right_div] == '0':
                right = float('inf')
            else:
                right = int(n[:right_div]) + int(n[right_div:])
            
            count += 1
            n = min(left, right)
        print("ASdasd", n)
        answer = [count, n]

    return answer

print(solution(90008))

from collections import deque

dir_x = [0, -1, 0, 1] # > v < ^ 순
dir_y = [1, 0, -1, 0]

def solution(maze):
    i = 0    
    maze_lim = len(maze)
    visited = [[False] * len(maze) for _ in range(len(maze))]

    queue = deque()
    queue.append((0, 0, 0)) # 좌표, 진행방향
    count = -1
    while queue:
        
        x, y, cur_dir = queue.popleft()
        print("q방문", x, y, cur_dir, queue)
        visited[x][y] = True
        count += 1

        if x == maze_lim - 1 and y == maze_lim - 1:
            break

        # 방향에 따라 direction 체인지
        # 4가지 방향 탐색(왼쪽 벽 우선순위)
        temp_queue = deque()
        for i in range(4):
            
            d = (cur_dir -i + 1) % 4
            
            nx = x + dir_x[d]
            ny = y + dir_y[d]
            
            # print(i, d, nx, ny)
            # 맵안에 있고 벽이 아닌 경우
            if 0 <= nx < maze_lim and 0 <= ny < maze_lim and maze[nx][ny] != 1:
                
                # 방문한 지점이 아니면 
                if not visited[nx][ny]:
                    queue.append((nx, ny, d))
                    break
                # 갈 곳이 없는 경우
                else:
                    temp_queue.append((nx, ny, d))
        
        if len(queue) == 0:
            queue.append(temp_queue.popleft())
            
            
    print(count)
    return count

solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]])