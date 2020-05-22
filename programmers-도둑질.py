'''
링크: https://programmers.co.kr/learn/courses/30/lessons/42897
풀이방법
- Dynamic Programming
- 첫번째와 마지막이 연결되면 안되므로 첫번째 집을 털 경우와 마지막 집을 털 경우를 나누어서 진행한다.
- 초기값을 넣어주는 것이 중요하다.
- i-1번째를 털었을 경우: dp[i-1], i-1번째를 털지 않을 경우: dp[i-2] + money[i]

'''
def solution(money):
    
    n = len(money)
    
    # 첫번째 집을 털 경우
    dp = [0] * n
    # 0번째 집을 털었으므로 1번째 집을 털지 못한다.
    dp[0] = money[0]
    dp[1] = money[0] 
    
    for i in range(2, n - 1):
        a = dp[i-2] + money[i]
        b = dp[i-1]
        dp[i] = max(a, b)
    
    # 마지막 집을 털었을 경우
    dp2 = [0] * n
    # 첫번째 집을 털지 않는다
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, n):
        a = dp2[i-2] + money[i]
        b = dp2[i-1]
        dp2[i] = max(a, b)
        
    # print(dp, dp2)
    return max(max(dp), max(dp2))

# 눈여겨 볼만한 풀이
def solution(a):
    x1, y1, z1 = a[0], a[1], a[0]+a[2]
    x2, y2, z2 = 0, a[1], a[2]
    for i in a[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)
