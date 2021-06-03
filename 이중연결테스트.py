class DLinkedList() :
    class Node() :
        def __init__ (self, v, n=None, p=None) :
            self.value = v
            self.next = n
            self.prev = p

    def __init__(self) :
        self.head = None
        self.tail = None

    def insertModeBefore(self,v):
        if self.head is None:
            self.head = self.Node(v)
            self.tail = self.head
        else:
            self.head.prev = self.Node(v,n=self.head)
            self.head = self.head.prev

    def insertModeAfter(self,v):
        if self.tail is None:
            self.tail = self.Node(v)
            self.head = self.tail
        else:
            self.tail.next = self.Node(v,p=self.tail)
            self.tail = self.tail.next

    def printNodeBefore(self):
        if self.head is None:
            print("데이터 없음")
            return
        else:
            print("현재 전화번호부", end='\t')
            link = self.head

            while link :
                print(link.value, '/' , end='')
                link = link.next
            print()

    def printNodeAfter(self):
        if self.tail is None:
            print("데이터 없음")
            return
        else:
            print("현재 전화번호부", end="\t")
            link = self.tail

            while link :
                print(link.value, '/' , end='')
                link = link.prev
            print()
            
    def deleteNodeBefore(self):
        if self.head is None:
            print("삭제할 데이터 없음")
            return
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteNodeAfter(self):
        if self.tail is None:
            print("삭제할 데이터 없음")
            return
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def searchBefore(self,v):
        if self.head is None:
            print("데이터 없음")
            return
        else:
            link = self.head
            index = 0
            while link:
                if v == link.value:
                    return index
                else:
                    link = link.next
                    index += 1

    def searchAfter(self,v):
        if self.tail is None:
            print("데이터 없음")
            return
        else:
            link = self.tail
            index = -1
            while link:
                if v == link.value:
                    return index
                else:
                    link = link.prev
                    index -= 1





#전체 전화번호부 확인
def printNodes(start) :
    current = start
    if current == None :
        return
    print(current.data, end='')
    while current.link != None : #마지막 노드까지 ->
        #즉 링크가 가리키는 노드가 없을때까지 반복한다.
        current = current.link #current를 현 위치 노드 link로 변경
        print(current.data, end='')
    print()

#데이터 삭제
def deleteMode(namePhone) :
    global head, current, pre

    if head == None:
        print("삭제할 노드가 없음")
        return False

    if head.data[0] == namePhone :
        current = head
        head = head.link
        del(current)
        return True

    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data[0] == namePhone :
            pre.link = current.link
            #노드가 하나 삭제되며 앞의 링크가 삭제 링크의 다음 링크를 가리킨다.
            del(current)
            #현재 노드가 차지하고 있던 데이터 삭제
            return True

    return False

#연락처 갱신
def updateNode(namePhone) : 
    global contact, head, current, pre

    current=head
    if head.data[0] == name:
            updateNum = input("연락처 수정: ")
            current.data[1] = updateNum #[1]은 연락처가 저장된 위치이다.
            #즉 [0]에 저장된 이름을 찾고 [1]의 내용을 갱신한다.
            return current
        
    while current.link != None:
            current = current.link
            if current.data[0] == name:
                    updateNum = input("연락처 수정: ")
                    current.data[1] = updateNum
                    return current

    else :
        print("없는 이름입니다.")
    
#데이터 검색
def findNode(namePhone) :
    global contact, head, current, pre

#입력값이 있으면 그에 대한 정보 출력
    current = head
    if current.data[0] == namePhone :
        return current.data[1]
    while current.link != None :
        current = current.link
        if current.data[0] == namePhone :
            return current.data[1]
    else :
        print("없는 이름입니다.")
    return Node()

#전화번호부 추가
def insertNodeBefore(self, data) :

    if self.head is None :
        self.head = self.Node(v)
        self.tail = self.head #같은 노드를 가리킨다.
    else :
        self.head.prev = self.Node(data, next=self.head)
        self.head = self.head.prev
    
    contact.append(node) #새로운 노드값이 전화번호부에 삽입된다.
    if head == None :
        head = node
        return

    if head.data[1] > namePhone[1] :
        node.link = head
        head = node
        return

    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data[1] > namePhone[1] :
            pre.link = node
            node.link = current
            return

    current.link = node

contact = []
head, current, pre = None, None, None

if __name__ == "__main__" :

    while True :
        print("       [연결리스트 관리] \n1:입력/ 2:삭제/ 3:수정/ 4:탐색/ 5:종료")
        odr = int(input("1~5번 중 선택 : "))
        if odr == 1 :
            name = input("이름-->")
            if name == "" or name == None :
                print("이름 미입력")
            pnum = input("연락처-->")
            makeSimpleLinkedList([name, pnum])
            printNodes(head)
        elif odr == 2 :
            name = input("삭제할 이름-->")
            if name == "" or name == None :
                print("이름 미입력")
            deleteMode(name)
            printNodes(head)
        elif odr == 3 :
            name = input("이름-->")
            if name == "" or name == None :
                print("이름 미입력")
            updateNode(name)
            printNodes(head)
        elif odr == 4 :
            name = input("이름-->")
            if name == "" or name == None :
                print("이름 미입력")
            findNode(name)
            printNodes(head)
        elif odr == 5 :
            exit()
        else :
            print("재입력하시오.")
