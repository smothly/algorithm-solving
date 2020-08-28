'''
프로그래머스 가장 긴 팰린드롬
링크: https://programmers.co.kr/learn/courses/30/lessons/12904
풀이방법
- 딱히 풀이방법으로 표현할 게 없다.
- 기준점을 보내주어 기준점 기준으로 팰린드롬을 검사한다.
- 홀수 / 짝수 두가지 방법을 검사해야 한다.
- 출처: https://inspirit941.tistory.com/entry/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-Level-3
'''
    
def palindrome(s, left, right):
    # 팰린드롬이 나올 수 있는 경우의 수 3가지
    # aba: 홀수
    # abba: 짝수
    # aaa: 홀수이지만 같음
    
    # 왼쪽 오른쪽이 같을 경우 계속 진행
    while 0 <= left and right <= len(s) and s[left] == s[right-1]:
        left -= 1
        right += 1
    return s[left+1:right-1]

def solution(s):
    
    # 길이가 1이거나 문자 전체가 팰린드롬 일경우 연산 x
    if len(s) < 2 or s == s[::-1]:
        return len(s)
    
    # 역순으로 진행 
    # 홀수 / 짝수 두가지로 진행된다.
    result = ""
    for i in range(len(s)-1):
        # print(i, palindrome(s, i, i+1), palindrome(s, i, i+2))
        # 길이 기준으로 result update
        result = max(result, palindrome(s, i, i+1), palindrome(s, i, i+2), key = len)
    
    return len(result)