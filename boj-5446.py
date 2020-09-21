'''
백준 5446번 용량 부족
링크: https://www.acmicpc.net/problem/5446
풀이방법
- 
'''

from sys import stdin
stdin = open("input.txt", "r")
# T: 테스트 케이스 개수
T = int(stdin.readline())
for t in range(T):
    # N1: 지워야 하는 파일 개수
    N1 = int(stdin.readline())
    remove = [stdin.readline().strip() for _ in range(N1)]

    # N2: 지우지 말아야 하는 파일 개수
    N2 = int(stdin.readline())
    no_remove = [stdin.readline().strip() for _ in range(N2)]

    print(remove)
    print(no_remove)
