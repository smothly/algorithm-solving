'''
링크: https://programmers.co.kr/learn/courses/30/lessons/49191
풀이방법
- 각 선수의 이기고 지는 기록을 set으로 관리한다.
- 지는 결과들을 보고 이기는 결과를 추가하고, 반대로 이기는 결과를 보고 지는 결과를 추가한다.
'''

def solution(n, results):
    
    win = {x:set() for x in range(1, n+1)}
    lose = {x:set() for x in range(1, n+1)}
    
    # 경기 결과 기록하기
    for w, l in results:
        win[w].add(l)
        lose[l].add(w)
        
    # 각 결과를 보고 연관있는 것들 업데이트 
    for i in range(1, n+1):
        for w in lose[i]:
            win[w].update(win[i])
        for l in win[i]:
            lose[l].update(lose[i])
    
    # 결과 알 수 있는 개수 리턴
    answer = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1
        
    return answer