'''
백준 1916번 최소 비용 구하기
링크: https://www.acmicpc.net/problem/1916
풀이방법
- 다익스트라 출처: https://jjangsungwon.tistory.com/28
'''

from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict

stdin = open("input.txt", "r")
edges = defaultdict(lambda: [])

def dijkstra(start, end):
    heap = []
    heappush(heap, (0, start))  # 시작지점 힙에 추가
    distance = [float('inf')] * (N + 1)  # 각 정점사이의 거리 무한대로 초기화
    distance[start] = 0  # 시작 지점 0으로 초기화   
    print(edges)
    while heap:
        cost, index = heappop(heap)
        if(distance[index] < cost) : continue # 검사할 필요 없음
        for e, c in edges[index]:
            if distance[e] > cost + c:
                distance[e] = cost + c
                heappush(heap, (cost + c, e))
    return distance[end]

# N 도시의 개수
# M 버스의 개수
N = int(stdin.readline()) 
M = int(stdin.readline()) 

# (출발 도시, 도착 도시, 버스 비용) M개
for _ in range(M):
    start, end, cost = map(int, stdin.readline().split())
    edges[start].append((end, cost))

# 시작지점, 끝 지점
start_city, end_city = map(int, stdin.readline().split())
    
print(dijkstra(start_city, end_city))

# 플로이드 와샬: 모든정점에서 모든정정 최단거리 https://blog.naver.com/ndb796/221234427842
# 크루스칼: MST 모든정점을 잇는 최소의 값 https://www.fun-coding.org/Chapter20-kruskal-live.html
# 다익스트라: 한 정점에서 모든 정점 최단거리: https://www.fun-coding.org/Chapter20-shortest-live.html
