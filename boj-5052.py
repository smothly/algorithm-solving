'''
백준 5052번 전화번호 목록
링크: https://www.acmicpc.net/problem/5052
풀이방법
- 
'''

from sys import stdin
stdin = open("input.txt", "r")
# T: 테스트 케이스 개수
T = int(stdin.readline())
for t in range(T):
    # N: 전화번호 갯수
    N = int(stdin.readline())

    # 입력 받고 정렬
    phone_numbers = [stdin.readline().strip() for _ in range(N)]
    phone_numbers.sort()

    flag = 0
    for i in range(len(phone_numbers) - 1):
        # 접두어인지 확인
        if phone_numbers[i+1].startswith(phone_numbers[i]):
            print("NO")
            flag = 1
            break
    if flag == 0: print("YES")
    