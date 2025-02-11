class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # LinkedList 의 가장 끝에 있는 노드에 새로운 노드를 연결
    def append(self, value):
        cur = self.head # 처음 노드를 먼저 검사
        while cur.next is not None: # 가장 끝의 노드는 현재노드.next가 None 임을 이용
            cur = cur.next # 옆 노드를 계속 검사
        cur.next = Node(value) # 끝에 도달하면 새로운 노드 생성

    # linked_list에서 저장한 head를 따라가면서 현재 있는 노드들을 전부 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

linked_list = LinkedList(5)
linked_list.append(6)
linked_list.append(7)

linked_list.print_all() # [5] -> [6] -> [7]