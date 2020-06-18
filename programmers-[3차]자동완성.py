'''
링크: https://programmers.co.kr/learn/courses/30/lessons/17685?language=python3
풀이방법
- 정렬한 후에 인접한 두 단어가 가장 비슷한 단어기 때문에 두 단어와만 비교해주면 된다.
- 두 단어를 비교해주는 함수를 잘 짜면 된다. 
- 트라이 설명 https://hooongs.tistory.com/28
'''

def prefix(w1, w2, w3):
    
    # w2의 단어 입력에 필요한 문자 수를 얻기위함
    
    # w1과 w2 비교
    i = 0
    a = 0
    while True:
        if i == len(w1):
            a += 1
            break
        elif i == len(w2):
            break 
        
        # 같으면 추가
        if w1[i] == w2[i]:
            a += 1
            i += 1
        else:
            a += 1
            break
    
    # w2와 w3 비교
    i = 0
    b = 0
    while True:
        if i == len(w3):
            b += 1
            break
        elif i == len(w2):
            break 
        
        # 같으면 추가
        if w2[i] == w3[i]:
            b += 1
            i += 1
        else:
            # if len(w3) < len(w2):
            b += 1
            break
        
    # 둘중에 max값
    return max(a, b)

def solution(words):
    
    # 자동완성
    # 앞부분이 같으면 다른 문자가 나올 때까지 입렵
    # 각 단어를 찾을려면 몇 글자를 입력해야하는지
    
    answer = 0
    # 트라이구조랑 sort해서 푸는 2가지 방식 나는 sort
    words.sort()   
    
    # 맨 첫 값하고 마지막 값 처리 먼저
    answer += prefix(words[-1], words[0], words[1])
    answer += prefix(words[-2], words[-1], words[0])
    
    # 이제 가운데에 있는 단어들 검사
    for i in range(1, len(words) - 1):
        answer += prefix(words[i-1], words[i], words[i+1])

    return answer