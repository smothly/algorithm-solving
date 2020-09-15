'''
백준 2533번 최소 비용 구하기
링크: https://www.acmicpc.net/problem/2533
풀이방법
- 
'''

import sys
from sys import stdin
from collections import defaultdict

sys.setrecursionlimit(10**9)

def DFS(cur):
    check[cur]=False
    DP[cur][0]=1 #현재 노드 포함할 때
    DP[cur][1]=0 #현재 노드 포함하지 않을 때
    for i in edges[cur]:
        if check[i]:
            DFS(i)
            DP[cur][0]+=DP[i][1]
            DP[cur][1]+=max(DP[i][0], DP[i][1])


stdin = open("input.txt", "r")

# N 도시의 개수
N = int(stdin.readline()) 

edges = defaultdict(lambda: [])
# (u, v) N-1개
for _ in range(N-1):
    u, v = map(int, stdin.readline().split())
    # 양방향 추가
    edges[u].append(v)
    edges[v].append(u)

DP = [[0, 0] for _ in range(N+1)]
check = [True for _ in range(N+1)]
DFS(1)

print(N - max(DP[1][0], DP[1][1]))

# DP(i) = i 를 root로 하는 subtree 의 최소 얼리 어답터 수

# 하지만 2가지 경우로 나뉨 
# 현재 노드가 얼리어답터 -> 인접한 다음 노드 얼리어답터 x
# 현재 노드가 얼리어답터 x -> 인접한 다음 노드는 얼리어답터 or x

# j를 추가
# j = i가 얼리어답터인지 아닌지
# 출처: https://www.weeklyps.com/entry/BOJ-2533-사회망-서비스 [weekly ps]
i = 노드번호, j =
# DP( i, j ) = i의 상태가 j인 경우, i 를 root로 하는 subtree 의 최소 얼리 어답터 수 


print(edges)