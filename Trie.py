# trie 자료구조
# 문자열 탐색할 때나 공통 부분 찾을 때 많이 쓰임

from collections import deque

class Node(object):
    
    def __init__(self, key, data=None):
        self.key = key
        self.data = data # leaf node는 전체 데이터, 나머지 node들은 글자 1개를 담고 있다.
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
    
    def search(self, string):
        cur = self.head
        
        for char in string:
            # 하위 노드에 해당 캐릭터가 있는지 확인 하면서 하위노드 쭉 순회 
            if char in cur.children:
                cur = cur.children[char]
            else:
                return False
            
        # 끝까지 왔고 완벽한 string이 있으면 완벽한 문자열
        if (cur.data != None):
            return True
    
    def starts_with(self, prefix):
        cur = self.head
        result = []
        subtrie = None
        
        # prefix의 마지막 캐릭터가 어디있는지 찾고
        # subtrie에 넣음으로 prefix로 시작되는 시작 지점을 찾아냄.
        # ex) prefix = abc -> c가 subtrie지점이 되어 abcd abcde 이러한 문자열을 찾아냄
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
                subtrie = cur
            else:
                return None
        
        # bfs를 사용해서 하위노드들을 계속 순회하여 prefix로 시작하는 항목들 가져오기
        queue = deque(list(subtrie.children.values()))
        while queue:
            curr = queue.popleft()
            if curr.data != None:
                result.append(curr.data)
            
            queue.extend(list(curr.children.values()))
                
        return result
        
        
# Test
t = Trie()
words = ["romane", "romanus", "romulus", "ruben", 'rubens', 'ruber', 'rubicon', 'ruler']
for word in words:
    t.insert(word)

print(t.search("romulus"))
print(t.search("ruler"))
print(t.search("rulere"))
print(t.search("romunus"))
print(t.starts_with("ro"))
print(t.starts_with("rube"))