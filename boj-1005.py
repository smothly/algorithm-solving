'''
백준 1005번 ACM Craft
링크: https://www.acmicpc.net/problem/1005
풀이방법
- Dynamic Programming + 위상 정렬
- queue를 이용하여 우선순위 없는 것들만 큐에 넣어가며 도착지까지의 건설 시간을 구한다.
'''

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 입력받기
    N, K = map(int, input().split())
    construction_time = [0] + list(map(int, input().split()))
    # 정답 풀기 위한 리스트들  
    DP = [0 for i in range(N+1)] # dp적용 각 건물의 최종 건설 시간
    order = [[] for i in range(N+1)] # 다음 방문
    inD= [0 for i in range(N+1)] # 진입 차수

    # 초기 세팅: order에는 순서 건물 짓는 순서 넣어주고 inD는 진입 차수
    for i in range(K):
        a,b = map(int, input().split())
        order[a].append(b) # a 다음 b
        inD[b] += 1 # 진입차수 + 1

    dest = int(input())

    # 우선순위가 필요 없는 경우(진입차수가 없는 경우) 시작 큐에 넣어줌
    queue = []
    for i in range(1, N+1):
        if inD[i] == 0:
            queue.append(i)

    # 도착지에 진입차수가 없어질 때 까지
    while inD[dest] > 0:
        
        p = queue.pop(0)

        # 다음 방문 order를 진입차수 줄이고 큐에 추가
        for i in order[p]:
            # 진입차수 줄이고 
            inD[i] -= 1
            # 걸리는 시간 업데이트 dp
            DP[i] = max(DP[i], DP[p] + construction_time[p])
            if inD[i] == 0:
                queue.append(i)
    print(DP[dest] + construction_time[dest])