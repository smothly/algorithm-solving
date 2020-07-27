'''
프로그래머스 보석쇼핑 2020 카카오 인턴십
링크: https://programmers.co.kr/learn/courses/30/lessons/67258
풀이방법
- 투 포인터
- 모든 보석이 들어있을 때까지 end를 증가시킨다.
- 모든 보석이 있으면 start를 증가시키며 최소 거리를 찾는다.
- 길이로 끝까지 갔는지 확인을 하고, 개수를 dict로 관리한다.
'''

from collections import defaultdict

def solution(gems):
    # 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
    # 시작과 끝번호 출력
    answer = [0, len(gems)]
    start, end = 0, 0
    gem_len, gem_kind = len(gems), len(set(gems))
    
    count_dict = defaultdict(int)
    count_dict[gems[0]] = 1
    
    while start < len(gems) and end < len(gems):
        # 모든 보석이 들어왔을 경우
        # 제거할 수 있는 보석이 있는 지 확인 한다.
        if len(count_dict) == gem_kind:
            # 최소거리일 경우
            if answer[1] - answer[0] > end - start:
                answer = [start + 1, end + 1]
            
            count_dict[gems[start]] -= 1
            if count_dict[gems[start]] == 0:
                del count_dict[gems[start]]
            start += 1
        # 모든 보석이 없을 경우
        # end를 1칸 증가 시켜준다.
        else:
            end += 1
            if end == gem_len:
                break
            count_dict[gems[end]] += 1
    return answer