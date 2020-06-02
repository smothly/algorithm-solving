'''
백준 16235번 나무제테크
링크: https://www.acmicpc.net/problem/16235
풀이방법
- 
-
'''

from collections import defaultdict

def spring():
    # 나이만큼 양분 먹고 나이가 1 증가
    # 여러 개 나무 있으면 
    for r in range(N):
        for c in range(N):
            if MAP[r][c] != 0:
                return



import sys
sys.stdin = open("input.txt", "r")

# 입력받기
N, M, K = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 처음에 양분 맵
MAP = [[5] * N for _ in range(N)]

# 여러개가 있을 수 있어서 리스트 딕트
trees = defaultdict(lambda: [])
tree_count = 0

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    tress[(x-1, y-1)].append(z)
    tree_count += 1

for k in range(K):
    spring()
    summer()
    fall()
    winter()

print(A, trees)