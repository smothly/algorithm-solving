'''
링크: https://programmers.co.kr/learn/courses/30/lessons/12983
풀이방법
- 설명: https://programmers.co.kr/learn/courses/18
- Dynamic Programming
- 역순으로 돌아 각 단어가 strs에 있거나 이전dp값이 존재하면 dp업데이트
'''

def solution(strs, t):
    answer = 0
    t_len = len(t)

    # dp 초기화
    dp = [float('inf')] * (t_len + 1)
    dp[t_len] = 0 # 마지막 값을 0으로 해놔야 dp가 작동한다.
    
    # 역순으로 진행
    for i in range(t_len - 1, -1, -1):

        tmp = ''
        # 1 ~ 5까지 단어조각으로 조건이 주어짐
        for j in range(6):
            if (i + j) >= t_len:
                break

            tmp = t[i + j]

            # 단어가 strs에 속하거나 이전 dp값이 존재하면
            if tmp in strs and dp[i + j + 1] != float('inf'):
                # 뒤에 값으로 
                dp[i] = min(dp[i], dp[i + j + 1] + 1)


    if (dp[0] == float('inf')):
        return -1

    return dp[0]
