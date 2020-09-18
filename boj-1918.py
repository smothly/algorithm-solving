'''
백준 1918번 후위 표기식
링크: https://www.acmicpc.net/problem/1918
풀이방법
- 스택

'''

# 중위 표기식을 후위 표기식으로 변환


# 알파벳 대문자와 +, -, *, /, (, ) 로만 이루어짐
import sys
from sys import stdin
from collections import deque

stdin = open("input.txt", "r")
stack = deque()

operator = ['+', '-', '*', '/']

priority = {
    "*": 2, "/": 2,
    "+": 1, "-": 1,
    "(": 0
}
# 중위 표현식 입력
infix = stdin.readline().strip()

answer = ""
for char in infix:
    # 여는 괄호면 stack에 쌓아놓기
    if char == "(":
        stack.append(char)
    # 닫는 괄호면 여는 괄호가 나올 때까지 팝하기
    elif char == ")":
        while stack and stack[-1] != "(":
            answer += stack.pop()
        stack.pop()
    # 연산자면 스택 내부 살피기
    # 우선순위를 봐서 높거나 같으면 출력
    elif char in operator:
        while stack and priority[char] <= priority[stack[-1]]:
            answer += stack.pop()
        stack.append(char)
    # 문자면 바로출력
    else:
        answer += char

# 나머지 팝
while stack:
    answer += stack.pop()

print(answer)

