'''
링크: https://programmers.co.kr/learn/courses/30/lessons/42627
풀이방법
- 각 디스크를 [요청 시간, 걸리는 시간]순으로 sort한다.
- 요청시간이 끝나는 시간보다 적을경우와 커지는 경우만 잘 나누면 된다.
'''

def solution(jobs):
    answer = 0
    
    # 더 빨리 끝나는거 먼저 수행 하면 된다.
    jobs.sort(key=lambda x: (x[0], x[1]))
    num_jobs = len(jobs)
    start, time = jobs.pop(0)
    end = time+start
    answer += time
    
    while jobs:
        
        next_index = 0
        # 다음 요청 인덱스 찾기
        for i in range(1, len(jobs)):
            # 끝난 지점보다 시작 지점이 커지면
            if jobs[i][0] > end:
                break
            # 끝난 지점보다 시작 지점이 작아지면
            else:
                # 시간이 작은걸로 
                if jobs[i][1] < jobs[next_index][1]:
                    next_index = i
        
        next = jobs.pop(next_index)

        # 시작지점이 end보다 작거나 같을 경우만
        if next[0] <= end:
            # 다음지점으로 선택
            answer += next[1] + (end - next[0])
            end += next[1]
        # 시작 > end면 
        else:
            # 다음지점 선택 더하기
            answer += next[1]
            end = sum(next) # 시작 지점 부터 끝까지니까..
    
    return answer // num_jobs