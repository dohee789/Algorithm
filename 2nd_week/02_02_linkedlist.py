class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# node = Node(3)
# next_node = Node(4) # 이어줄 노드 생성
# node.next = next_node # 이어주기 [3] -> [4]
# print(node.data, node.next.data)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # linked_list 의 가장 끝에 있는 노드에 새로운 노드를 연결
    def append(self, value):
        cur = self.head  # 처음 노드를 먼저 검사
        while cur.next is not None:  # 가장 끝의 노드는 현재노드.next가 None 임을 이용
            cur = cur.next  # 옆 노드를 계속 검사
        cur.next = Node(value)  # 끝에 도달하면 새로운 노드 생성

    # linked_list 에서 저장한 head를 따라가면서 현재 있는 노드들을 전부 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value) # 추가할 새로운 노드 생성 : [4]

        if index == 0:
            new_node.next = self.head  # 기존 head를 새로운 노드의 next로 지정
            self.head = new_node  # 새 노드를 head로 만듦
            return
        prev_node = self.get_node(index - 1) # index-1 번째의 노드 뒤에 생성해야 하기 때문에 : node = [3]
        next_node = prev_node.next # 추가한 노드 뒤에 이어질 노드 찾기 (linked_list 에는 head 정보만 담고 있기 때문)
        prev_node.next = new_node # 앞노드에 새로운 노드 이어주고 : [3] -> [4]
        new_node.next = next_node # 새로운 노드랑 뒷노드 이어주고 : [4] -> [5]

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)
        prev_node.next = index_node.next


linked_list = LinkedList(3)
linked_list.append(5)
linked_list.add_node(0, 2)
linked_list.add_node(2, 4)
linked_list.print_all()