'''
swea 5656번 벽돌 깨기
링크: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo&
풀이 방법
- 끝나는 조건: n번이 끝나거나 맵이 전부 0이거나
- 
'''


def find(n, COUNT, MAP):
    global MIN

    # n번이 끝나거나 1이 아닌 것이 1개도 없거나
    if n == N or not COUNT:
        MIN = min(MIN, COUNT)
        return
  
    for w in range(W):
        q = []
        # 처음 부술 블럭 찾기
        for i in range(H):
            if MAP[i][w]:
                # 복사
                data = [j[:] for j in MAP]
                cnt = COUNT - 1
                # 위치랑 값 queue에 쌓아놓기
                q = [(i, w, data[i][w])]
                print(q)
                data[i][w] = 0
                break
        # 큐 없으면 다음 col 찾기

        if not q:
            continue
  
        # 블록 부수기
        while q:
            y, x, length = q.pop()
            # length만큼
            for k in range(1, length):
                for dy, dx in (0, 1), (0, -1), (1, 0), (-1, 0):
                    ny = y + dy * k
                    nx = x + dx * k
                    # 맵안에 있고 값이 있을 때 부술 블럭에 추가
                    if -1 < ny < H and -1 < nx < W and data[ny][nx]:
                        if data[ny][nx] > 1:
                            q.append((ny, nx, data[ny][nx]))
                        
                        data[ny][nx] = 0
                        cnt -= 1
  
        # 떨어지기
        for x in range(W):
            idx = H - 1 # 인덱스를 마지막 값으로 두고 0이 나타나면  index 감소
            for y in range(H - 1, -1, -1):
                if data[y][x]:
                    # 스왑
                    data[idx][x], data[y][x] = data[y][x], data[idx][x]
                    idx -= 1
        find(n + 1, cnt, data)
  
import sys
sys.stdin = open("input.txt", "r")
  
T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]
    count = sum(1 for x in MAP for a in x if a) # 0이 아닌 개수들

    MIN = 9999
    find(0, count, MAP)
    print("#{} {}".format(tc, MIN))
    break


'''
import copy
from collections import deque


def gravity():


direction = ((1, 0), (0, 1), (-1, 0), (0, -1)) # ^ > v < 순
def boom(x, y):
    k = MAP[x][y]
    MAP[x][y] = 0
    
    # 크기가 1보다 클경우만 해주면 된다.
    if k > 1:
        for d in direction:
            cur_x, cur_y = x, y
            for j in range(k-1):
                move_x = qx + d[0]
                move_y = qy + d[1]
                if 0 <= move_x < W and 0 <= move_y < H and MAP[cur_x][cur_y] > 1:
                    boom((cur_x, cur_y))
                else:
                    MAP[cur_x][cur_y] = 0

    return

def dfs(depth):
    # 마지막 까지 왔을 경우
    if depth == N:
        _sum = 0
        for i in range(H):
            for j in range(W):
                if MAP[i][j]: _sum += 1
        if _sum < answer:
            answer = _sum
        return
    
    temp = copy.deepcopy(MAP)
    check = 0

    # 반대로 가로 부터 검사 해야한다
    for j in range(W):
        for i in range(H):
            # 0일경우
            if MAP[i][j]: break
        # i가 끝일 경우 패스
        if i == h:
            continue
        check = 1
        boom((i, j))
        gravity()
        dfs(depth+1)
        MAP = copy.deepcopy(temp)
    
    if not check:
        answer = 0


    
import sys
import numpy as np
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 입력 받기
    N, W, H = map(int, input().split())
    MAP = np.array([np.array(list(map(int, input().split()))) for x in range(H)])
    # visited = [[False] * W for _ in range(H)]


    

    dfs(0)            
    # marbles.append((i, boom_marble_index(W[:, i])))


    print('#{} {}'.format(test_case, answer))

    break
'''