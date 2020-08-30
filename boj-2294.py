'''
백준 2294번 동전 2
링크: https://www.acmicpc.net/problem/2294
풀이방법
- Dynamic Programming
'''

from sys import stdin
stdin = open("input.txt", "r")
# 숫자 입력
n, k = map(int, stdin.readline().split())

# 입력 받고 중복 제거후 정렬
coins = [int(stdin.readline()) for _ in range(n)]
coins = list(set(coins))
coins.sort()

# dp배열 선언 최대값(10001)
dp = [10001] * (k+1)
dp[0] = 0

# 1, 5, 12원 loop
for i in coins:
    # ex) 5원 차례면 5, 15 까지 loop
    for j in range(i, k+1):
        # dp[j] = 기존 값 / dp[j - i] + 1 = 이전에 만들 수 있는 값 + 1
        dp[j] = min(dp[j], dp[j - i] + 1)

# 값을 못 만들경우 처리
if dp[k] == 10001: print(-1)
else: print(dp[k])