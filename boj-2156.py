'''
백준 2156번 포도주 시식
링크: https://www.acmicpc.net/problem/2156
풀이방법
- Dynamic Programming
'''


import sys

# sys.stdin = open("input.txt", "r")

# 입력
N = int(input())
wines = [int(input()) for _ in range(N)]

# DP를 돌리기 위한 첫번째 element 0
wines.insert(0, 0)

# dp 초기화
dp = [0 for i in range(N+1)]
dp[0] = wines[0]
dp[1] = wines[0] + wines[1]

answer = 0
# 3가지 경우이다.
# 1. n번째 와인을 마시지 않는 경우: X
# 2. n번째 와인을 마시고 n-2번의 최대: OXO
# 3. n번째 n-1번째 와인을 마시고 n-3번의 최대: OXOO
for i in range(2, N + 1):
    a = dp[i-1]
    b = dp[i-2] + wines[i]
    c = dp[i-3] + wines[i-1] + wines[i]
    dp[i] = max(a, b, c)

print(dp[-1])
    
    

    