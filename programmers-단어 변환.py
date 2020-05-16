'''
링크: https://programmers.co.kr/learn/courses/30/lessons/43162
풀이방법
- BFS
- 하나만 바뀌는 경우 단어들을 queue에 추가하여 bfs 돌린다.
- target단어로 만들어지면 return
'''

def solution(begin, target, words):
    
    # target 없으면
    if target not in set(words):
        return 0
    
    queue = [begin]
    total_count = 0
    
    # 단어가 전부 없을 때 까지
    while len(words) != 0:
        # 각 단어들을 검사
        for value in queue:
            temp = []
            # 1글자 다른 단어인지 체크하는 과정
            for word in words:
                count = 0
                for i in range(len(word)):
                    if value[i] != word[i]:
                        count += 1
                    elif count == 2:
                        break
                # 하나만 변해도 가능한 경우 
                if count == 1:
                    temp.append(word)
                    words.remove(word)
                    
        total_count += 1
        # target단어가 만들어질 수 있으면
        if target == "".join(temp):
            return total_count
        else:
            queue = temp # 바꿀 수 있는 단어들을 추가
            
    return 0