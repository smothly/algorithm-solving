'''
링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4yLUiKDUoDFAUx&categoryId=AV4yLUiKDUoDFAUx&categoryType=CODE&&&
문제풀이방식: BFS를 stack을 사용하여

'''

def solution(map_, visit, test, r, c):
    dx = [-1, 0, 1, 0] # 밑 왼쪽 위 오른쪽
    dy = [0, -1, 0, 1]
    stack = [[0, 0, 3, 0]]
    while stack:
        # x,y는 좌표 d는 direction m은 memory값 이다.
        x, y, d, m = stack.pop()
        if visit[x][y][d][m] == test:
            continue
        else:
            visit[x][y][d][m] = test
            # 왼쪽으로 갈경우
            if map_[x][y] == '<' or (map_[x][y] == '_' and m != 0):
                # %r 과 %c를 해주는 이유는 초과하면 0으로 가기 때문
                stack.append([(x + dx[1]) % r, (y + dy[1]) % c, 1, m])
            elif map_[x][y] == '>' or (map_[x][y] == '_' and m == 0):
                stack.append([(x + dx[3]) % r, (y + dy[3]) % c, 3, m])
            elif map_[x][y] == '^' or (map_[x][y] == '|' and m != 0):
                stack.append([(x + dx[0]) % r, (y + dy[0]) % c, 0, m])
            elif map_[x][y] == 'v' or (map_[x][y] == '|' and m == 0):
                stack.append([(x + dx[2]) % r, (y + dy[2]) % c, 2, m])
            elif map_[x][y] == '@': # 정지할 수 있는 경우
                return True
            elif map_[x][y] == '+':
                # d 방향으로 간다 / 마지막에 16나눠주는 이유는 15이상이면 0으로 가야하기때문에
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, (m + 1)%16])
            elif map_[x][y] == '-':
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, (m - 1)%16])
            elif map_[x][y] == '.':
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, m])
            # ?같은경우는 4방향이 전부 가능하다는 소리다. 그래서 4방향을 전부 스택에 추가해준다.
            elif map_[x][y] == '?':
                for i in range(4):
                    stack.append([(x + dx[i]) % r, (y + dy[i]) % c, i, m])
            # 숫자일 경우 저장하고 그대로 진행방향
            else:
                stack.append([(x + dx[d]) % r, (y + dy[d]) % c, d, int(map_[x][y])])
    return False

import sys
sys.stdin = open("input.txt", "r")
T = int(input())

# 왜 visit를 처음에 4차원으로 해주는지..?
visit = [[[[0 for _ in range(16)] for _ in range(4)] for _ in range(20)] for _ in range(20)]

for test_case in range(1, T + 1):
    r, c = map(int, input().split())
    map_ = [input() for _ in range(r)]
    answer = solution(map_, visit, test_case, r, c)
    
    if answer == True:
        answer = "YES"
    else:
        answer = "NO"
    
    print('#{} {}'.format(test_case, answer))
