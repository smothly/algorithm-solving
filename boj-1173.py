'''
백준 1173번 운동
링크: https://www.acmicpc.net/problem/1173
풀이방법
- 운동할 수 없는 경우만 잘 파악하고 최대 맥박 관리만 잘 해주면 된다.
'''
import sys
# sys.stdin = open("input.txt", "r")

N, m, M, T, R = map(int, input().split())
cnt = 0
X = m
# 운동 할 수 없는 경우
if X + T > M:
    cnt = -1
else:    
    while N:
        cnt += 1
        # 운동
        if X + T <= M:  
            X += T
            N -= 1
        # 휴식
        else:      
            X -= R
            if X < m:
                X = m
print(cnt)