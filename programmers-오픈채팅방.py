'''
링크: https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
풀이방법
- 파이썬 내장 dict와 list만 잘 쓰면 되는 문제다.
- 최종 id:nickname을 저장해놓고 변환해서 쓰면 된다.
'''

def solution(record):
    answer = []
    temp = []
    id_nick = dict()
    action = {}
    
    for r in record:
        r = r.split(" ")        
        # 일단 id로 다 너넣고 마지막에 id에 따른 nick을 출력해주면 되겠네
        if r[0] == "Leave":
            temp.append((r[0], r[1]))
        else:
            # dict 에 추가
            id_nick[r[1]] = r[2]
            if r[0] == "Enter":
                temp.append((r[0], r[1]))
    for cmd, user_id in temp:
        if cmd == "Leave":
            answer.append(id_nick[user_id] + "님이 나갔습니다.")            
        else:
            answer.append(id_nick[user_id] + "님이 들어왔습니다.")
        
    return answer