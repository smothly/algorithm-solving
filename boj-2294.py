'''
백준 2294번 동전 2
링크: https://www.acmicpc.net/problem/2294
풀이방법
- 
'''

from sys import stdin
stdin = open("input.txt", "r")
# 숫자 입력
n, k = map(int, stdin.readline().split())

# 입력 받고 중복 제거후 정렬
coins = [int(stdin.readline()) for _ in range(n)]
coins = list(set(coins))
coins.sort()

# dp배열 선언
dp = [10001] * (k+1)
dp[0] = 0

print(dp)

for i in coins:
    
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j - i] + 1)

    print(dp)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])