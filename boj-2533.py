'''
백준 2533번 사회망 서비스(SNS) 
링크: https://www.acmicpc.net/problem/2533
풀이방법
- 트리 DP
- 어렵다... 
'''

import sys
from sys import stdin

sys.setrecursionlimit(10**9)

def DFS(cur):
    visited[cur] = True
    for i in edges[cur]:
        if not visited[i]:
            child[cur].append(i)
            DFS(i)

def get_dp(cur, check):
    if check: # 얼리어답터면
        # DP( i, true) = min(DP(i 의 자식, true), DP(i 의 자식, false))들의 총합 + 1
        if dp[cur][1] != -1:
            return dp[cur][1]
        dp[cur][1] = 1 # 본인이 얼리어답터니 + 1을 해주는 것이다.
        for i in child[cur]: # 하위 노드 탐색
            dp[cur][1] += min(get_dp(i, False), get_dp(i, True))
        return dp[cur][1]
    else: # 얼리어답터가 아니며
        # DP( i, false) = DP(i 의 자식, true) 들의 총합 
        if dp[cur][0] != -1:
            return dp[cur][0]
        dp[cur][0] = 0 # 얼리어답터가 아니므로 0
        for i in child[cur]: # 하위 노드 탐색
            dp[cur][0] += get_dp(i, True) #
        return dp[cur][0]


stdin = open("input.txt", "r")

# N 노드의 개수
N = int(stdin.readline()) 

edges = [[] for _ in range(N+1)]
child = [[] for _ in range(N+1)]

# (u, v) N-1개
for _ in range(N-1):
    u, v = map(int, stdin.readline().rstrip().split())
    # 양방향 추가
    edges[u].append(v)
    edges[v].append(u)

dp = [[-1, -1] for _ in range(N+1)] # dp 초기화
visited = [False] * (N+1)

print(min(get_dp(1, False), get_dp(1, True)))
# DP(i) = i 를 root로 하는 subtree 의 최소 얼리 어답터 수

# 하지만 i가 얼리어답터인지 아닌지에 따라 2가지 경우로 나뉨
# 1. 현재 노드가 얼리어답터 -> 인접한 다음 노드 얼리어답터 x
# 2. 현재 노드가 얼리어답터 x -> 인접한 다음 노드는 얼리어답터 or x

# j 추가 -> i가 얼리어답터인지 아닌지의 여부

# 최종 점화식
# DP( i, true) = min(DP(i 의 자식, true), DP(i 의 자식, false))들의 총합 + 1
# i 가 얼리어답터면은 자식 노드가 얼리어답터인 경우와 아닌 경우 두 부분을 구해야 함
# 여기에 root가 얼리 어답터니까 + 1

# DP( i, false) = DP(i 의 자식, true) 들의 총합 
# i 가 얼리어답터가 아닌 경우는 자식 노드는 무조건 얼리어답터 여야함

# 출처: https://www.weeklyps.com/entry/BOJ-2533-사회망-서비스 [weekly ps]