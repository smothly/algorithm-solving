'''
백준 16235번 나무제테크
링크: https://www.acmicpc.net/problem/16235
풀이방법
- 빡구현 문제
- 핵심은 여러개의 나무를 한좌표안에 갖고 있는 것이다...
'''

from collections import defaultdict

direction = [[-1,0],[0,-1],[1,0],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]
def year():
    # 봄 & 여름
    for (r, c), tree in trees.items():
        tree.sort()
        temp_tree = []
        sumv = 0
        for t in tree:
            # 나이만큼 양분먹기
            if t <= board[r][c]:
                board[r][c] -= t
                temp_tree.append(t + 1)
            # 양분 부족 -> 여름에 나이를 2로나눈 값이 양분으로 추가
            else:
                sumv += t//2

        trees[(r, c)] = temp_tree
        board[r][c] += sumv

    # 가을
    new_tree = []
    for (r, c), tree in trees.items():
        for t in tree:
            if t%5 == 0:
                for d in direction:
                    move_r = r + d[0]
                    move_c = c + d[1]
                    if 0 <= move_r < N and 0 <= move_c < N:
                        new_tree.append((move_r, move_c))
    for r, c in new_tree:
        trees[(r, c)].append(1)
    
    # 겨울
    for r in range(N):
        for c in range(N):
            board[r][c] += A[r][c]


import sys
sys.stdin = open("input.txt", "r")

# 입력받기
N, M, K = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 처음에 양분 맵
board = [[5] * N for _ in range(N)]

# 여러개가 있을 수 있어서 리스트 딕트
trees = defaultdict(lambda: [])

# 나무 입력
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[(x-1, y-1)].append(z)

# 제테크 진행
for k in range(K):
    year()

# 나무 개수 출력
print(sum([len(tree) for tree in trees.values()]))