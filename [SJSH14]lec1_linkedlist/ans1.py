

# 1번 정답
class Stu:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.next = None
    def insertNext(self, next):
        self.next = next

Cholsoo = Stu('철수', 1)
Yeonghee = Stu('영희', 2)

# 철수의 다음에 영희가 등장. 철수가 head node가 된다.
Cholsoo.insertNext(Yeonghee)

# 아래는 linked list 전체 프린트하는 함수.

# def printLinkedList(headnode):
#     printedNode = headnode
#     while (printedNode != None):
#         print(printedNode.name, printedNode.number)
#         printedNode = printedNode.next


# 2번 정답

def nInsert(n, name, number, headnode):
    insertedStu = Stu(name, number)
    detectStu = headnode
    for i in range(n-1):
        detectStu = detectStu.next
    insertedStu.insertNext(detectStu.next)
    detectStu.insertNext(insertedStu)
    return headnode

# nInsert(0, '범수', 3,Cholsoo)
# printLinkedList(Cholsoo)

# 3번 정답
def nDelete(n, headnode):
    detectStu = headnode
    for i in range(n-2):
        detectStu = detectStu.next
    detectStu.insertNext(detectStu.next.next)
    return headnode

# nDelete(2, Cholsoo)
# printLinkedList(Cholsoo)