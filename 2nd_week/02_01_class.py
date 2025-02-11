class Person:
    def __init__(self, name_param):
        self.name = name_param
        print("HI", self, self.name)

    def talk(self):
        print("안녕하세요 저는", self.name, "입니다")

person_1 = Person("남궁민")
person_1.talk()
person_2 = Person("안은진")
person_2.talk()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
next_node = Node(4) # 이어줄 노드 생성
node.next = next_node # 이어주기 [3] -> [4]