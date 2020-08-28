'''
프로그래머스 올바른 괄호
링크: https://programmers.co.kr/learn/courses/30/lessons/12929
풀이방법
- 카탈란 수
'''


# 
from math import factorial
def solution(n):
    return factorial(2*n) // (factorial(n) * factorial(n)*(n+1))
