'''
백준 3190번 뱀
링크: https://www.acmicpc.net/problem/3190
풀이방법
- 빡구현
- 본인 몸에 닿는 것 확인 + 사과 먹으면 0으로 바꿔주기
- direction을 잘 바꿔주는지 확인
'''


import sys
sys.stdin = open("input.txt", "r")

# 입력
N = int(input())
MAP = [[0]*N for _ in range(N)]

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    MAP[x-1][y-1] = 1

L = int(input())
dir_change = [input().split() for _ in range(L)]
max_di = len(dir_change)
dir_index = 0
cur_dir = 0

time = 0

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

snake = [(0, 0)]

while True:
    time += 1

    # 진행방향 대로
    move_x = snake[-1][0] + direction[cur_dir][0]
    move_y = snake[-1][1] + direction[cur_dir][1]

    if 0 <= move_x < N and 0 <= move_y < N and (move_x, move_y) not in snake[:-1]:
        snake.append((move_x, move_y))
        # 사과가 있으면
        if MAP[move_x][move_y] == 1:
            MAP[move_x][move_y] = 0
        # 없으면
        else:
            snake.pop(0)

    # 벽에 부딪힐 경우 몸이랑 부딪히는 경우
    else:
        print(time)
        sys.exit(0)
    
    # 방향 전환
    if dir_index < max_di:
        if time == int(dir_change[dir_index][0]):
            if dir_change[dir_index][1] == 'L':
                cur_dir = (cur_dir - 1) % 4
            else:
                cur_dir = (cur_dir + 1) % 4
            dir_index += 1






