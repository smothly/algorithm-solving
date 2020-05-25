'''
백준 2252번 줄세우기
링크: https://www.acmicpc.net/problem/2252
풀이방법
- 위상정렬
- 진입차수 list와 다음 순서를 저장하는 dict를 선언해서 푼다.
'''

import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())

ind = [0 for _ in range(N+1)]
path = defaultdict(lambda: []) # 다음 방문

for i in range(M):
    # B가 더 키가 큰 친구이다. 
    A, B = map(int, input().split())
    # A 다음 B이다.
    path[A].append(B)
    ind[B] += 1

# 진입차수 0인 것들 먼저 큐에 저장
queue = []
for i in range(1, N+1):
    if ind[i] == 0:
        queue.append(i)
 
while queue:
    p = queue.pop(0)
    print(p, end=' ')
    
    for i in path[p]:
        ind[i] -= 1
        if ind[i] == 0:
            queue.append(i)
