'''
백준 5446번 용량 부족
링크: https://www.acmicpc.net/problem/5446
풀이방법
- Trie
'''
class Node(object):
    
    def __init__(self, key, mark=0, data=None):
        self.key = key
        self.mark = mark
        self.data = data # leaf node는 전체 string, 나머지 node들은 None을 담고 있다.
        self.children = {}
        
class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        cur = self.head
        
        for char in string: # 각 캐릭터 순회
            # 해당 캐릭터가 트리에 없을경우 하위 노드로 추가
            if char not in cur.children: 
                cur.children[char] = Node(char)                
            cur = cur.children[char] # 현재 노드 변경

        # 마지막 노드의 경우 data를 스트링으로 변경하여 마지막 노드임을 명시
        cur.data = string    
    
    def marking(self, string):
        # insert 과정과 유사하나 삭제하지 말아야 하는 부분에 mark를 1로 설정한다.
        cur = self.head
        
        for char in string:
            cur.mark = 1
            if char not in cur.children:
                cur.children[char] = Node(char) 
            cur = cur.children[char]
        cur.mark = 1

    def remove(self, string):
        cur = self.head
        
        result = 0
        for char in string:
            # 해당 캐릭터가 있고 해당 캐릭터가 mark가 되어있으면 계속 순회
            if char in cur.children and cur.children[char].mark == 1:
                cur = cur.children[char]
            # 이미 삭제한 부분이면 종료해도 된다. 상위 명령어로 전부 삭제 가능하기 때문이다.
            elif cur.children[char].mark == 2:
                return result
            # 삭제가능한 경우 mark를 2로 바꿔주고 return 해준다.
            else:
                result += 1
                cur.children[char].mark = 2
                # print(cur.children[char].key)
                return result
        
        result += 1
        return result        

from sys import stdin
stdin = open("input.txt", "r")
# T: 테스트 케이스 개수
T = int(stdin.readline())
for t in range(T):

    trie = Trie()
    # N1: 지워야 하는 파일 개수
    N1 = int(stdin.readline())
    remove_list = []
    for _ in range(N1):
        remove_list.append(stdin.readline().strip())
        trie.insert(remove_list[-1])

    # N2: 지우지 말아야 하는 파일 개수
    N2 = int(stdin.readline())
    for _ in range(N2):
        trie.marking(stdin.readline().strip())

    # 지우는 과정
    answer = 0
    for i in range(N1):
        temp = trie.remove(remove_list[i])
        # print(remove_list[i], temp)
        answer += temp

    # 출력
    if N2 == 0: print(1)
    else: print(answer)