'''
백준 1922번 네트워크 연결
링크: https://www.acmicpc.net/problem/1922 
풀이방법
- 크루스칼

'''

from sys import stdin

stdin = open("input.txt", "r")

def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)
    
    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1    
    
def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(vertices, edges):
    mst = list()
    
    # 1. 초기화
    for node in vertices:
        make_set(node)
    
    # 2. 간선 weight 기반 sorting
    edges.sort(key=lambda x: x[2]) # 비용순으로 sort
    
    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        node_v, node_u, weight = edge
        # 루트가 다를 경우 합쳐준다.
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(weight) # 합쳐줄 때 추가
    
    return sum(mst)
    
# N 컴퓨터의 개수
# M 선의 수
N = int(stdin.readline()) 
M = int(stdin.readline()) 

vertices = list(range(1, N+1))
parent = {}
rank = {}
    
# (a, b, c) M개
edges = [tuple(map(int, stdin.readline().rstrip().split())) for _ in range(M)]

print(kruskal(vertices, edges))    
