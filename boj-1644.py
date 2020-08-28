'''
백준 1644번 소수의 연속 합
링크: https://www.acmicpc.net/problem/1644
풀이방법
- 에라토스테네스의 체
- 투 포인터
'''

from sys import stdin
stdin = open("input.txt", "r")
# 숫자 입력
N = int(stdin.readline())

# 에라토스테네스의 체 
# 출처: https://leedakyeong.tistory.com/entry/python-소수-찾기-에라토스테네스의-체
prime = [True] * (N+1)
for i in range(2, int(N ** 0.5) + 1):
    if prime[i]==True:
        for j in range(i+i, N+1, i):
            prime[j]=False

# N이하의 소수 구하기
prime_list = [i for i in range(2, N+1) if prime[i]==True]

# 투 포인터 변수(start, end) / 현재 합 변수 / 정답 카운트
start, end, cur_sum, answer = 0, 0, 0, 0

length = len(prime_list)

while True:
    
    # 현재합이 N보다 커지면 왼쪽 포인터만 이동
    if N <= cur_sum:
        cur_sum -= prime_list[start]
        start += 1
    
    # while문 종료조건: 오른쪽 포인터가 끝까지 갔을 경우
    elif end == len(prime_list):
        break
    
    # 현재합이 N보다 작아지면 오른쪽 포인터만 이동
    else:
        cur_sum += prime_list[end]
        end += 1
    
    # 숫자와 같을경우 정답 카운트
    if N == cur_sum:
        answer += 1

print(answer)