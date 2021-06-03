class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    if current == None :
        return
    print(current.data, end='')
    while current.link != None :
        current = current.link
        print(current.data, end='')
    print()


def deleteMode(namePhone) :
    global dataArray, head, current, pre

    if head.data[0] == namePhone :
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data[0] == namePhone :
            pre.link = current.link
            del(current)
            return

def updateNode(namePhone) : #실패
    global dataArray, head, current, pre

    if head.data[0] == namePhone :
        current = head
        head = head.link
        current.data[1] = input("연락처 갱신 :") #갱신하면 값이 없다는 오류가 나옵니다.
        return

    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data[0] == namePhone :
            pre.link = current.link
            current.data[1] = input("연락처 갱신 :") #갱신하면 값이 없다는 오류가 나옵니다.
            return

def findNode(namePhone) :
    global dataArray, head, current, pre

    current = head
    if current.data[0] == namePhone :
        return current.data[1]
    while current.link != None :
        current = current.link
        if current.data[0] == namePhone :
            return current.data[1]
    return Node()

def makeSimpleLinkedList(namePhone) :
    global dataArray, head, current, pre

    node = Node()
    node.data = namePhone
    dataArray.append(node)
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

dataArray = []
head, current, pre = None, None, None

if __name__ == "__main__" :

    while True :
        print("       [연결리스트 관리] \n1:입력/ 2:삭제/ 3:수정/ 4:탐색/ 5:종료")
        odr = int(input("1~5번 중 선택 : "))
        if odr == 1 :
            name = input("이름-->")
            if name == "" or name == None :
                break
            pnum = input("연락처-->")
            makeSimpleLinkedList([name, pnum])
            printNodes(head)
        elif odr == 2 :
            name = input("삭제할 이름-->")
            if name == "" or name == None :
                break
            deleteMode(name)
            printNodes(head)
        elif odr == 3 :
            name = input("이름-->")
            if name == "" or name == None :
                break 
            updateNode(name)
            printNodes(head)
        elif odr == 4 :
            name = input("이름-->")
            if name == "" or name == None :
                break             
            findNode(name)
            printNodes(head)
        elif odr == 5 :
            exit()
        else :
            print("재입력하시오.")
