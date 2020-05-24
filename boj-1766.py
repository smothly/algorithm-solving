'''
백준 1766번 문제집
링크: https://www.acmicpc.net/problem/1766
풀이방법
- 위상정렬
- 진입차수 list와 다음 순서를 저장하는 dict를 선언해서 푼다.
- 하지만, 쉬운문제 조건이 있으므로 queue를 heapq로 선언하여 푼다.
'''


import sys
from collections import defaultdict
import heapq

# sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())

ind = [0 for _ in range(N+1)]
path = defaultdict(lambda: []) # 다음 방문

for i in range(M):
    A, B = map(int, input().split())
    path[A].append(B)
    ind[B] += 1

# 진입차수 0인 것들 먼저 큐에 저장
priority_queue = []
for i in range(1, N+1):
    if ind[i] == 0:
        heapq.heappush(priority_queue ,i)

while priority_queue:
    # 큐중에서 우선순위를 알아서 정해졌으므로 팝하면 된다.
    p = heapq.heappop(priority_queue)
    print(p, end=' ')

    for i in path[p]:
        ind[i] -= 1
        if ind[i] == 0:
            heapq.heappush(priority_queue ,i)


