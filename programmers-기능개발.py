'''
프로그래머스 기능개발
링크: programmers.co.kr/learn/courses/30/lessons/42586?language=python3 
풀이방법
- queue
'''
def solution(progresses, speeds):
    
    answer = []
    count = 0
    time = 0
    while progresses:
        # print(progresses, speeds, answer)
        
        # 맨 앞에 값이 100보다 커지면
        if (progresses[0] + time*speeds[0]) >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
                
    answer.append(count)
    return answer
