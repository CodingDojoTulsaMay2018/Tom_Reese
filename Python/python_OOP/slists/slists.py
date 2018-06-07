class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SList:
    def __init__(self,value):
        node=Node(value)
        self.head = node
    def addnode(self,value):
        node = Node(value)
        runner = self.head
        while runner.next != None:
            runner = runner.next 
        runner.next = node 
    def printallvals(self,msg=''):
        runner = self.head
        while runner.next != None:
            print(runner.value, runner.next.value)
            runner = runner.next
        print(runner.value,"is the last node")
    def removenode(self,value):
        mid = None
        target = Node(value)
        print("searching for",target.value)
        head = self.head
        print(head.value,"is the head")
        # print(head.value,"is the head node")
        # print(target.value,"is the last node I need")
        # if target.next == None:
        #     target.next = None
        if target == head:
          print("found the head, and it's",head.value)
          head.next = self.head
          target.next = None
          print(head.value,"is the new head")
          return self
        # while head != target:
        #     if head.next == target:
        #         target.next = mid
        #         head.next = target
        #     return self
        

list = SList(1)
list.addnode(7)
list.addnode(3)
list.addnode(73)
list.addnode("potatoe")
list.addnode([1,2,3])

# list.printallvals("attempt1")
# list.removenode([1,2,3])
# list.removenode(3)
list.removenode(1)