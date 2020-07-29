'''
링크: https://programmers.co.kr/learn/courses/30/lessons/42892
풀이방법
- 트리 순회 문제
- 트리를 구축하기 위한 전처리 y 내림차순 x 오름차순이 중요하다.
'''

import sys
sys.setrecursionlimit(10**9)

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data):
        
        if self.data:
            if data[1] < self.data[1]:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data[1] > self.data[1]:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    #     preorder
    #     # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data[0])
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data[0])
        return res

def solution(nodeinfo):
    
    # y값은 노드의 레벨
    # x 값은 left / right 순위

    # data, x, y 값으로 만들어 주고 y 내림차순 x 오름차순으로 정렬해주면
    # 트리구조로 인풋을 넣을 수 있다.
    nodeinfo = [(data+1, x, y) for data, (x, y)in enumerate(nodeinfo)] 
    nodeinfo.sort(key=lambda x: (-x[2], x[1]))
    
    root = Node(nodeinfo[0])
    for data in nodeinfo[1:]:
        root.insert(data)
        
    answer = []
    answer.append(root.PreorderTraversal(root))
    answer.append(root.PostorderTraversal(root))
    
    return answer