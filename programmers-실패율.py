'''
링크: https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3
풀이방법
- 잘 구현하면 된다..
- 실패율이 0일때만 잘 처리해주면 된다.
'''

from collections import defaultdict
def solution(N, stages):
    
    # 실패율 = 스테이지 클리어 x 인원 / 스테이지 도달 인원
    
    # 실패율이 높은 스테이지부터 출력
    # 동률일 경우는 스테이지가 낮은순
    
    # 알아야 할 것
    # 각 스테이지의 도달인원 
    # [스테이지 넘버, 실패율]
    
    
    # count 해서 key로 소트후 하나씩 만들어 주면 되겠네
    stage_user = defaultdict()
    # 모든 stage 0으로 초기화
    for i in range(1, N+2):
        stage_user[i] = 0
    for s in stages:
        stage_user[s] += 1
    stage_user = sorted(stage_user.items())
    
    # 각 stage의 실패율 계산하여 추가
    answer = []
    total = len(stages)
    for stage, user in stage_user[:-1]:
        if total == 0:
            answer.append((stage, 0))
        else:
            answer.append((stage, user/total))
            total -= user

    # 실패율과 stage순으로 정렬
    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [_[0] for _ in answer]
    # print(answer)
    return answer