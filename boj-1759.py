'''
백준 1759번 암호 만들기
링크: https://www.acmicpc.net/problem/1759
풀이방법
- 정렬 후 조합에서 각 조건을 검사해 주면 된다. 
'''

from sys import stdin

stdin = open("input.txt", "r")

# L: 암호 자릿 수
# C: 알파벳 개수
L, C = map(int, stdin.readline().split())

alphabets = stdin.readline().split()
alphabets.sort()

from itertools import combinations
comb = combinations(alphabets, L)

# 조건 1: 최소 1개의 모음
# 조건 2: 최소 2개의 자음
# 조건 3: 오름차순 정렬
mo = {'a', 'e', 'i', 'o', 'u'}
def check(password):

    j = set(password) - mo
    m = set(password).intersection(mo)
    # 조건1, 2 체크
    if len(j) < 2 or len(m) < 1:
        return False
    else:
        return True

for password in comb:
    if check(password): print(''.join(password))