'''
백준 1762번 평면그래프와 삼각형
링크: https://www.acmicpc.net/problem/1762
풀이방법
- 각 edge(u, v)를 순회하며 각 노드의 교집합이 있는지 확인한다.
'''


import sys

# sys.stdin = open("input.txt", "r")

# N, M 입력 
N, M = map(int, sys.stdin.readline().split())

# 1~N까지의 빈 set 선언
node_neighbors = [set() for i in range(N+1)]

answer = 0
for i in range(M):
    # Edge 입력
    u, v = map(int, sys.stdin.readline().split())
    # 교집합의 길이만큼 더해줌 
    answer += len(node_neighbors[u]&node_neighbors[v])
    # 각 노드의 이웃들 만들기
    # if u > v 조건 걸어줘도 됨
    node_neighbors[u].add(v)
    node_neighbors[v].add(u)

print(answer)
