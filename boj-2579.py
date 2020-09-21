'''
백준 2579번 계단 오르기
링크: https://www.acmicpc.net/problem/2579
풀이방법
- 다이나믹 프로그래밍
'''

from sys import stdin
stdin = open("input.txt", "r")
# N: 계단의 개수
N = int(stdin.readline())

stairs = [int(stdin.readline()) for _ in range(N)]

if N <= 2:
    print(sum(stairs))

else:
    DP = []
    DP.append(stairs[0]) # 첫번째 계단
    DP.append(stairs[0] + stairs[1]) # 두번째 계단 까지의 최댓값
    DP.append(max(stairs[2] + stairs[1], stairs[2] + stairs[0])) #세번째 계단은 1, 2 or 0, 2 두가지 경우로 이루어질 수 있음.

    for i in range(3, N):
        # print(DP)
        DP.append(stairs[i] + max(DP[i-2], stairs[i-1] + DP[i-3]))
    print(DP[-1])
