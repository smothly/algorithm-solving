'''
백준 2531번 회전 초밥
링크: https://www.acmicpc.net/problem/2531
풀이방법
- 모든 경우의 수에 대하여 초밥 가짓수를 구하여 max값을 리턴하면 된다. 
'''


###########
# 내 코드 # 
###########
import sys
from collections import deque
sys.stdin = open("input.txt", "r")

# 입력
N, d, k, c = map(int, input().split()) # 초밥 개수, 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
sushi = [int(input()) for i in range(N)]
sushi = sushi + sushi[:k] # 스시를 일렬로 쭉 펴주기

eaten = sushi[-k+1:] + sushi[:1]

answer = []
for i in range(N):
    sushi_count = set(sushi[i:i+k])
    count = len(sushi_count)
    if c not in sushi_count:
        count += 1
    answer.append(count)

print(max(answer))    

# 다른 사람 코드
# 시간차이가 많이나서 분석

def goRight(i):
    global now
    # 먹지 않은 거면 추가
    if count[i] == 0:
        now += 1
    # 먹은거 체크
    count[i] += 1

def goLeft(i):
    global now
    # 먹은 거 뱉음
    count[i] -= 1
    # 다 뱉었으면
    if count[i] == 0:
        now -= 1 

import sys
sys.stdin = open("input.txt", "r")

N, d, k, c = map(int, input().split()) # 초밥 개수, 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
sushi = [int(input()) for i in range(N)]
sushi = sushi + sushi[:k]

count = [0] * (d+1)
answer = 0
now = 0

goRight(c) # 쿠폰은 항상 먹는게 좋으므로

# 처음 먹는 걸로 초기화
for i in range(k-1):
    goRight(sushi[i])

for i in range(N):
    # 1칸씩 미뤄주는 과정이다.
    goRight(sushi[i+k-1]) # i ~ i+k 개 까지 먹는 거
    answer = max(answer, now)
    goLeft(sushi[i]) # i 번째 초밥 뱉음

print(answer)







