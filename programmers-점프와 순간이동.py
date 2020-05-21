'''
링크: https://programmers.co.kr/learn/courses/30/lessons/12980
풀이방법
- 2를 나눌 수 있는 경우 나눠주고 아니면 점프하면 된다. 
- 이진수로 변환하여 카운트하는 풀이법이 있다............
'''

def solution(n):
    ans = 0
    while n != 0:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            ans +=1
    return ans

def solution(n):
    return bin(n).count('1')